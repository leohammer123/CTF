# warm up 1
It seems that the link is broken, but we can find the source code at the bottom of the source code.
```javascript
function nono(e) {if (navigator.appName == 'Netscape' && (e.which == 3 || e.which == 2)) return false;
else if (navigator.appName == 'Microsoft Internet Explorer' && 
(event.button == 2 || event.button == 3)) { alert("oops");
return false;}return true;}
document.onmousedown=nono;document.onmouseup=nono;

function a(){
	thepw = 'warmup1';
	thepw = thepw+'lol';
	thepw = thepw + 'copter';
	if (document.lf.pw.value==thepw) {
		document.location = '/'+thepw; } else { alert('That is not correct. Please try again.');
	}
}

if (document.layers) window.captureEvents(Event.MOUSEDOWN);
if (document.layers) window.captureEvents(Event.MOUSEUP);
window.onmousedown=nono;window.onmouseup=nono;

document.lf.pw.focus();

```
It compared the user input and thepw variable.
# flag : 

# warm up 2

This level is broken,so just type fail
# warm up 

You have to post a non-exist option , that sounds impossible, but you can directly change client side source code in browser.

![picture]()