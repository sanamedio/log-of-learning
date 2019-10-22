# 23-oct-2019

### 1 - dbus notifications

```python
import dbus, dbus.proxies
#-- connect to the session bus (as opposed to the system bus)
session = dbus.SessionBus()

#-- create proxy object of D-Bus object
obj_proxy = dbus.proxies.ProxyObject(conn=session,
         bus_name="org.freedesktop.Notifications",     #-- name of the service we are retrieving object from
         object_path="/org/freedesktop/Notifications") #-- the object path

#-- create proxy object of the D-Bus object wrapped into specific interface
intf_proxy = dbus.proxies.Interface(obj_proxy, "org.freedesktop.Notifications")

#-- lastly, create proxy object of the D-Bus method
method_proxy = intf_proxy.get_dbus_method("Notify")

#-- ... and call the method
method_proxy("test from python",
             dbus.UInt32(0),
             "bluetooth",     #-- icon name
             "Notification summary",
             "Here goes notification body",
             [], {},
             500) #-- timeout) #-- timeout
```
