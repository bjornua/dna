<%inherit file="/main.mako" />
<h1>LAN</h1>
    <h3>Netværksadapter</h3>
    <table>
        <tbody>
            <tr>
                <td>
                    <label for="lan_address">Adresse</label>
                </td>
                <td>
                    <input type="text" id="lan_address" name="lan_address" value="10.0.72.1" />
                </td>
            </tr>
            <tr>
                <td>
                    <label for="netmask">Netmaske</label>
                </td>
                <td>
                    <input type="text" id="netmask" name="netmask" value="255.255.255.0" />
                </td>
            </tr>
        </tbody>
    </table>
    <h3>DHCP-Server</h3>
    <table>
        <tbody>
            <tr>
                <td>
                    <label for="dhcp_address_min">Minimum adresse</label>
                </td>
                <td>
                    <input type="text" id="dhcp_address_min" name="dhcp_address_min" value="10.0.72.10" />
                </td>
            </tr>
            <tr>
                <td>
                    <label for="dhcp_address_max">Maximum adresse</label>
                </td>
                <td>
                    <input type="text" id="dhcp_address_max" name="dhcp_address_max" value="10.0.72.254" />
                </td>
            </tr>
            <tr>
                <td>
                    <label for="dhcp_dns_1">Primær dns server</label>
                </td>
                <td>
                    <input type="text" id="dhcp_dns_1" name="dhcp_dns_1" value="8.8.8.8" />
                </td>
            </tr>
            <tr>
                <td>
                    <label for="dhcp_dns_2">Sekundær dns server</label>
                </td>
                <td>
                    <input type="text" id="dhcp_dns_2" name="dhcp_dns_2" value="8.8.4.4" />
                </td>
            </tr>
        </tbody>
    </table>
    <p>
        <input type="submit" value="Udfør ændring" />
    </p>

