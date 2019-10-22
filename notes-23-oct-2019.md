# 23-oct-2019



### 2 - listening to dbus 

- both the following didn't worked

```python
import gtk
import dbus
from dbus.mainloop.glib import DBusGMainLoop

def filter_cb(bus, message):
    # the NameAcquired message comes through before match string gets applied
    
    if message.get_member() != "Notify":
        return
    args = message.get_args_list()
    # args are
    # (app_name, notification_id, icon, summary, body, actions, hints, timeout)
    print("Notification from app '%s'" % args[0])
    print("Summary: %s" % args[3])
    print("Body: %s", args[4])


DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
bus.add_match_string(
    "type='method_call',interface='org.freedesktop.Notifications',member='Notify'")
bus.add_message_filter(filter_cb)
gtk.main()
```

```python
import dbus# Import Glib to setup an event loop which runs signal handlers.
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib


DBusGMainLoop(set_as_default=True)# Define the loop.
loop = GLib.MainLoop()


system_bus = dbus.SystemBus()

proxy_object = system_bus.get_object(
    'org.freedesktop.NetworkManager',
     '/org/freedesktop/NetworkManager'
)

def network_state_change_handler(new_state):
    print(new_state)


system_bus.add_signal_receiver(
    network_state_change_handler,
    signal_name='StateChanged',
    dbus_interface='org.freedesktop.NetworkManager'
)

loop.run()

```



### 1 - dbus send notifications

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
