from nicegui import ui, app

ui.dark_mode().enable()

ui.query('body').style('''
    background-color: #121212;
    margin: 0;
    padding: 0;
''')

ui.add_css('''
.close {
    position: fixed;
    top: 15px;
    left: 15px;
    width: 14px;
    height: 14px;
    background-color: #FF5F57;
    border: 1px solid #E0443E;
    border-radius: 50%;
    cursor: pointer;
    z-index: 9999;
}

.close:hover {
    background-color: #FF7770;
}

.fullscreen {
    position: fixed;
    top: 15px;
    left: 55px;
    width: 14px;
    height: 14px;
    background-color: #28C840;
    border: 1px solid #1AAB29;
    border-radius: 50%;
    cursor: pointer;
    z-index: 9999;
}

.fullscreen:hover {
    background-color: #50E060;
}
''')
is_maximized = False
def fullscreen():
    global is_maximized
    if is_maximized:
        app.native.main_window.restore()
    else:
        app.native.main_window.maximize()
    is_maximized = not is_maximized

ui.element('div').classes('close').on(
    'click', app.shutdown
)

ui.element('div').classes('fullscreen').on(
    'click', fullscreen
)

ui.run(
    native=True,
    frameless=True,
    window_size=(1200, 800),
    reload=False,
)