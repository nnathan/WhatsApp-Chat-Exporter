from Whatsapp_Chat_Exporter.utility import setup_template


def test_default_layout_is_narrow():
    html = setup_template(None, False).render(msgs=[])
    assert "width:430px" in html
    assert " width:100%;" not in html


def test_desktop_template_fills_window():
    html = setup_template("whatsapp_desktop.html", False, True).render(msgs=[])
    assert " width:100%;" in html
    assert "width:430px" not in html
