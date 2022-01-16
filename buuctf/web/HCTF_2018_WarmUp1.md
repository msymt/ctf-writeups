# [HCTF 2018]WarmUp 1

## 解放

ソース中に`<! souce.php>`があったため，`/source.php`にアクセスする．
'file'パラメータからcheckFileに渡してwhitelistによるチェックが行われている．
?より前がwhitelistに合致してもOkらしい．

`?file=hint.php`にアクセスすると`flag not here, and flag in ffffllllaaaagggg` とのヒントが得られた．

`?file=hint.php?ffffllllaaaagggg`と入力しても何も返ってこなかった．ディレクトリが違うと思い，相対パスで探索すると`/?file=hint.php?/../../../../ffffllllaaaagggg`でフラグを得られた．

## FLAG

```bash
flag{8c13925b-7a0b-488a-bfda-031c4a9e4e1d}
```

### source.php

```php
<?php
    highlight_file(__FILE__);
    class emmm
    {
        public static function checkFile(&$page)
        {
            $whitelist = ["source"=>"source.php","hint"=>"hint.php"];
            if (! isset($page) || !is_string($page)) {
                echo "you can't see it";
                return false;
            }

            if (in_array($page, $whitelist)) {
                return true;
            }

            $_page = mb_substr(
                $page,
                0,
                mb_strpos($page . '?', '?')
            );
            if (in_array($_page, $whitelist)) {
                return true;
            }

            $_page = urldecode($page);
            $_page = mb_substr(
                $_page,
                0,
                mb_strpos($_page . '?', '?')
            );
            if (in_array($_page, $whitelist)) {
                return true;
            }
            echo "you can't see it";
            return false;
        }
    }

    if (! empty($_REQUEST['file'])
        && is_string($_REQUEST['file'])
        && emmm::checkFile($_REQUEST['file'])
    ) {
        include $_REQUEST['file'];
        exit;
    } else {
        echo "<br><img src=\"https://i.loli.net/2018/11/01/5bdb0d93dc794.jpg\" />";
    }  
?>
```

## 参考

- https://graneed.hatenablog.com/entry/2018/11/11/211721
