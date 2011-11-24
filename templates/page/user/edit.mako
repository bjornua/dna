<%inherit file="/main.mako"/>
<h1>Bruger ${escape(username)}</h1>

%if len(errors) > 0:
<h3>Fejl</h3>
<ul id="createusererrors">
%if "macaddrs_max_type" in errors or "macaddrs_max" in errors:
    <li>MAC-Adresse antal skal være et tal større end 0.</li>
%endif
%if "passwordmatch" in errors:
    <li>De to indtastede adgangskoder var ikke ens.</li>
%endif
</ul>
%endif

<form action=${escattr(urlfor("user.edit_do", uid=uid))} method="POST">
<table>
<tbody>
    <tr>
        <td><label for="username">Brugernavn</label></td>
        <td>
            <input type="text" id="username" name="username" value=${escattr(username)}/>
        </td>
    </tr>
    <tr>
        <td><label for="email">E-mail</label></td>
        <td>
            <input type="text" id="email" name="email" value=${escattr(email)}/>
        </td>
    </tr>
    <tr>
        <td><label for="macaddrs_max">Antal MAC-adresser</label></td>
        <td>
            <input type="text" id="macaddrs_max" name="macaddrs_max" value=${escattr(str(macaddrs_max))} />
        </td>
    </tr>
    <tr>
        <td><label for="password0">Adgangskode</label></td>
        <td>
            <input type="password" id="password0" name="password0" />
        </td>
    </tr>
    <tr>
        <td><label for="password1">Gentag adgangskode</label></td>
        <td>
            <input type="password" id="password1" name="password1" />
        </td>
    </tr>
    <tr>
        <td colspan="2" style="text-align:right;">
            <input type="submit" value="Gem"/>
        </td>
    </tr>
</tbody>
</table>
<p>
    Efterlad adgangskodefeltet tomt for en autogenerere en adgangskode
</p>
</form>
