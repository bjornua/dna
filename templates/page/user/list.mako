<%inherit file="/main.mako" />
<h1>Brugere</h1>
<ul>
    <li><a href=${escattr(urlfor("user.create_form"))}>Tilføj bruger</a></li>
</ul>
<table>
    <thead>
        <tr>
            <th>Brugernavn</th>
            <th>E-mail adresse</th>
            <th>IP-Adresse</th>
            <th>MAC-Adresse</th>
            <th>Slet</th>
        </tr>
    </thead>
    <tbody>
%for uid, username, email, macaddrs in users:
        <tr>
            <td><a href=${escattr(urlfor("user.edit_form", uid=uid))}>${escape(username)}</a></td>
            <td><a href=${escattr("mailto:" + email)}">${escape(email)}</a></td>
            <td>Ikke implementeret</td>
            <td>${escape(", ".join(macaddrs))}</td>
            <td><a href=${escattr(urlfor("user.delete", uid=uid))}>[Slet]</a></td>
        </tr>
%endfor
    </body>
</table>
