import coverage
from django.test.runner import DiscoverRunner
from django.core.management import call_command

from apps.user.tests.test import retrieve_test_results
from common.test.view_test_mapping import views_to_update


class CustomTestRunner(DiscoverRunner):
    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        result = super().run_tests(test_labels, extra_tests, **kwargs)
        coverage_percentage = get_test_coverage()
        update_api_documentation(coverage_percentage)
        return result


def update_api_documentation(coverage_percentage):
    """_summary_

    Args:
        coverage_percentage (_type_): _description_
    """
    for view, test_case in views_to_update:
        view_doc = view.__doc__
        updated_doc = view_doc

        api_tests_passed = get_api_tests_passed(view, test_case)
        updated_doc = updated_doc.replace("{api_tests_passed}", str(api_tests_passed))

        test_coverage = coverage_percentage
        updated_doc = updated_doc.replace("{test_coverage}", str(test_coverage))

        view.__doc__ = updated_doc
    # call_command('runserver')


def get_test_coverage():
    """"""
    # Measure code coverage using the coverage library
    cov = coverage.Coverage()
    cov.start()
    cov.load()
    cov.stop()
    cov.save()
    coverage_percentage = cov.report(omit="*/tests.py")  # Adjust to exclude test files

    return coverage_percentage


def get_api_tests_passed(view, test_case):
    """_summary_

    Args:
        view (_type_): _description_
        test_case (_type_): _description_

    Returns:
        _type_: _description_
    """
    test_case_instance = test_case()
    test_results = retrieve_test_results()

    view_test_results = test_results.get(view.__name__, {})
    return view_test_results  # Replace with your logic


if __name__ == "__main__":
    test_runner = CustomTestRunner()
    test_runner.run_tests([])
