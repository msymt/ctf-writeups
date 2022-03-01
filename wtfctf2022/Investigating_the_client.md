# Investigating the client

75

Challenge description to go up on the website. A very secure login form that can be opened only if you have the required password.

Author: Swati Verma

## 解法

devtoolsからソースを見ると、4文字ずつ比較していました。
base64でデコードすると`d3RmQ1RGe2MxaTNudF9zMWQzX2wwZzFufQ==` -> `wtfCTF{c1i3nt_s1d3_l0g1n}`となりました。

```
function validate(){
    const pass = document.getElementById('password').value;
    split = 4;
    if(pass.substring(0,split) == 'd3Rm'){
        if (pass.substring(split,split*2) == 'Q1RG'){
            if(pass.substring(split*2,split*3) == 'e2Mx'){
                if(pass.substring(split*3,split*4) == 'aTNu'){
                    if(pass.substring(split*4,split*5) == 'dF9z'){
                        if(pass.substring(split*5,split*6) == 'MWQz'){
                            if(pass.substring(split*6,split*7) == 'X2ww'){
                                if(pass.substring(split*7,split*8) == 'ZzFu'){
                                    if(pass.substring(split*8,split*9) == 'fQ=='){
                                        alert("Correct Password, Hint:hint.html");
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    else{
        alert('Incorrect Password');
    }
}
```

## FLAG

```bash
wtfCTF{c1i3nt_s1d3_l0g1n}
```
