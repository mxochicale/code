# Examples 

## Running scripts
```
conda activate bareVE
python *.py 
```

## Debugging using the terminal

```
sudo apt-get install libxcb-cursor-dev
#export QT_QPA_PLATFORM=offscreen #>qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
#sudo apt purge ibus #qt.dbus.integration: Could not connect "org.freedesktop.IBus" to globalEngineChanged(QString)
kill -9 $(ps aux | grep 'python ' | grep -v 'grep')
```

## References
* pglive: https://github.com/domarm-comat/pglive/tree/main/pglive/examples_pyside6 