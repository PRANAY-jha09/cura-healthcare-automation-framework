import os

SCREENSHOT_DIR ="screenshots"

os.makedirs(SCREENSHOT_DIR,exist_ok=True)

def capture_screenshot(driver,test_name):
    path=os.path.join(
        SCREENSHOT_DIR,
        f"{test_name}.png"
    )

    driver.save_screenshot(path)
    return path