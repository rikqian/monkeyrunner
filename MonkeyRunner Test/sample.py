'''
Created on 2014/6/25
@author: Administrator
'''
from  com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

# 'emulator-5554' rick_nexusone
# 'HT237TD01843' htc
devices1=MonkeyRunner.waitForConnection(5,"emulator-5554")

#wake the device
devices1.wake()
#install the 163 news client
#devices1.installPackage('E:/Android/apps/com.netease.newsreader.activity.apk')
#devices1.installPackage('E:/Android/apps/ViewServer.apk')
# 
package = 'com.netease.newsreader.activity'
activity = 'com.netease.nr.phone.main.MainActivity'
runComponent = package + '/' + activity
devices1.startActivity(component = runComponent)
 
devices1.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)
#get a screenshot
MonkeyRunner.sleep(2)
screen1=devices1.takeSnapshot()
screen1.writeToFile('E:/Android/workspace/MR Test/MonkeyRunner Test/screenshot/s2.png','png')  

#click the News icon
devices1.touch(49,71,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)

devices1.drag((125,86),(7,86),0.5,10)

#logon
devices1.touch(443,70,MonkeyDevice.DOWN_AND_UP)
devices1.touch(443,70,MonkeyDevice.DOWN_AND_UP)