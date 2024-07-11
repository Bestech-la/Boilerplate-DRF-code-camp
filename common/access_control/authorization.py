from rest_framework import permissions
import casbin

enforcer = casbin.Enforcer(
    "common/access_control/model.conf", "common/access_control/policy.csv"
)


class CasbinAuthorization(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user  # Assuming you use Django's built-in User model
        groups = list(user.groups.values_list("name", flat=True))

        if user.is_anonymous:
            groups = ["anonymous"]

        resource, action = transform_path_to_resource_action(
            request.path, request.method
        )
        if user.is_superuser:
            return True
        allowed = enforcer.enforce(groups, resource, action)
        print(allowed)
        return allowed


def transform_path_to_resource_action(path, http_method):
    """
    Transforms a URL path and HTTP method into a resource and action.

    :param path: The URL path.
    :param http_method: The HTTP method (e.g., GET, POST, PUT, DELETE).

    :return: A tuple (resource, action) representing the resource and action.
    """
    parts = path.split("/")
    last_segment = parts[LAST_SEGMENT_INDEX]

    if last_segment.isdigit() and http_method in ["GET", "PATCH", "PUT", "DELETE"]:
        resource = parts[RESOURCE_SEGMENT_INDEX] + "/" + last_segment
        if http_method == "GET":
            action = "show"
        else:
            action = HTTP_METHOD_TO_ACTION.get(http_method, "unknown")
    else:
        resource = parts[RESOURCE_SEGMENT_INDEX] if last_segment == "" else last_segment
        action = HTTP_METHOD_TO_ACTION.get(http_method, "unknown")

    return resource, action


HTTP_METHOD_TO_ACTION = {
    "GET": "list",
    "POST": "create",
    "PATCH": "edit",
    "PUT": "edit",
    "DELETE": "delete",
}

LAST_SEGMENT_INDEX = -1
RESOURCE_SEGMENT_INDEX = -2
