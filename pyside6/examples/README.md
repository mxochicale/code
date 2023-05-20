# Examples 

## Running scripts
```
conda activate bareVE
python *.py 
```

## Debugging using the terminal

```
export QT_QPA_PLATFORM=offscreen #>qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
sudo apt purge ibus #qt.dbus.integration: Could not connect "org.freedesktop.IBus" to globalEngineChanged(QString)
#This plugin does not support propagateSizeHints()
kill -9 $(ps aux | grep 'python ' | grep -v 'grep')

```
