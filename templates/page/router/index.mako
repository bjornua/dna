<%inherit file="/main.mako" />
<%
from app.utils.numberformat import format_size

bytes_downloaded = 525441434
bytes_uploaded = 24222106


bytes_downloaded = format_size(bytes_downloaded)
bytes_uploaded = format_size(bytes_uploaded)


%>
<h1>Routing</h1>
<h3>Statistik</h3>
<table>
    <thead>
        <tr><th>Retning</th><th>Trafikmængde</th></tr>
    </thead>
    <tbody>
        <tr><td>WAN->LAN (Download)</td><td>${bytes_downloaded}</td></tr>
        <tr><td>LAN->WAN (Upload)</td><td>${bytes_uploaded}</td></tr>
    </tbody>
</table>
<h3>Kontrol</h3>
<p>
    <ul>
        <li>
            <a href="${urlfor("routing.open")}">Åben for internet routing</a>
        </li>
        <li>
            <a href="${urlfor("routing.close")}">Luk for internet routing</a>
        </li>
    </ul>
</p>
