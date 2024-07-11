from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response

def swagger_post_list(title, serializer):
    return swagger_auto_schema(
        operation_description="post single or list of "+ str(title),
        request_body=serializer(many=True),
        responses={status.HTTP_201_CREATED: serializer(many=True)},
    )
    
def post(instance, model, request, *args, **kwargs):
    is_many = isinstance(request.data, list)

    if not is_many:
        return super(model, instance).create(request, *args, **kwargs)
    else:
        serializer = instance.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        instance.perform_create(serializer)
        headers = instance.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)