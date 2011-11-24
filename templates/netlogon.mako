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
        <h1>Internet login</h1>
%if error:
        <h3 style="color:red;">Fejl</h3>
        <p style="color:red;">
            Enten brugernavn eller adgangskode er ikke korrekt indtastet.
        </p>
%endif
        <form method="POST" action=${escattr(urlfor("netlogon.login_do"))}>
        <table><tbody>
            <tr>
                <td><label for="username">Brugernavn</label></td>
                <td><input name="username" id="username" type="text"/></td>
            </tr>
            <tr>
                <td><label for="password">Adgangskode</label></td>
                <td><input name="password" id="password" type="password"/></td>
            </tr>
            <tr>
                <td colspan="2" style="text-align:right;"><input value="Log ind" type="submit"/></td>
            </tr>
        </tbody></table>
        </form>
    </div>
</body>
