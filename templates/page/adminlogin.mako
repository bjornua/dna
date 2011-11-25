<%inherit file="/main.mako"/>
<h1>Admin login</h1>
<p>
<form action=${escattr(urlfor("admin.login_do"))} method="POST">
<table>
<tr>
    <td><label for="password">Indtast adgangskode</label></td>
    <td><input type="password" id="password" name="password" /></td>
</tr><tr>
    <td colspan="2"><input type="submit" value="Log ind"></td>
</td><tr>
</table>
</form>
