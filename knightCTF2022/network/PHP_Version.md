# PHP Version

## description

25

What version of php the server is using?

Use Compromised CTF Platform's Challenge file to analyze.

Flag Format: KCTF{php/version}

Author : TareqAhamed

## writeup

`robots.txt`をFile->Export Objects->HTTPから取得する。すると、`PHP/7.4.27`と記載されていた。

```html
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>Object not found!</title>
<link rev="made" href="mailto:you@example.com" />
<style type="text/css"><!--/*--><![CDATA[/*><!--*/ 
    body { color: #000000; background-color: #FFFFFF; }
    a:link { color: #0000CC; }
    p, address {margin-left: 3em;}
    span {font-size: smaller;}
/*]]>*/--></style>
</head>

<body>
<h1>Object not found!</h1>
<p>


    The requested URL was not found on this server.

  

    If you entered the URL manually please check your
    spelling and try again.

  

</p>
<p>
If you think this is a server error, please contact
the <a href="mailto:you@example.com">webmaster</a>.

</p>

<h2>Error 404</h2>
<address>
  <a href="/">192.168.1.4</a><br />
  <span>Apache/2.4.52 (Unix) OpenSSL/1.1.1m PHP/7.4.27 mod_perl/2.0.11 Perl/v5.32.1</span>
</address>
</body>
</html>
```

## FLAG

```txt
KCTF{PHP/7.4.27}
```
