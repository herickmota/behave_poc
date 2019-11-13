from behave import given, when, then
from features.modules.page_objects import Google


@given('that I access Google')
def access_google_page(context):
    context.google = Google(context.driver)
    context.google.navigate()


@when('I insert "{value}" and press enter')
def search_the_value(context, value):
    context.google.search(value)


@then('the "{value}" result is displayed in the title')
def verify_result(context, value):
    context.google.check_search(value)
