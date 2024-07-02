def after_all(context):
    print("~~~~~~~~~~~ Navigate to C:\\Users\\<YourUsername>\\ and look for course_report.txt ~~~~~~~~~~~")
    if context.driver:
        context.driver.quit()
