
from web_ui.base import Base

class TestWindow(Base):
    def test_window(self):

        self.driver.switch_to.frame('frame_id') #使用frame_id切换到对应的frame
        self.driver.switch_to.parent_frame("") #切换到父frame
        self.driver.switch_to.default_content()  #切换到默认frame
