<%inherit file="/html5.mako"/>
<head>
    <title>DIKULAN Netværks Adminitration</title>
    <link rel="stylesheet" type="text/css" href="/static/css/main.css" />
</head>
<body>
    <div id="page">
        <div id="header">
            <h1>DIKULAN Netværks Administration</h1>
        </div>
        <hr/>
        <ul>
            <li><a href="${url_for("routing.index")}">Router</a></li>
            <li><a href="${url_for("firewall.index")}">Firewall</a></li>
            <li><a href="${url_for("user.index")}">Brugere</a></li>
            <li><a href="${url_for("lan.index")}">LAN</a></li>
            <li><a href="${url_for("wan.index")}">WAN</a></li>
        </ul>
        <hr />
        ${next.body()}
    </div>
</body>
