webpackJsonp([0],{"//Fk":function(t,r,e){t.exports={default:e("U5ju"),__esModule:!0}},"2KxR":function(t,r){t.exports=function(t,r,e,n){if(!(t instanceof r)||void 0!==n&&n in t)throw TypeError(e+": incorrect invocation!");return t}},"3fs2":function(t,r,e){var n=e("RY/4"),o=e("dSzd")("iterator"),i=e("/bQp");t.exports=e("FeBl").getIteratorMethod=function(t){if(void 0!=t)return t[o]||t["@@iterator"]||i[n(t)]}},"82Mu":function(t,r,e){var n=e("7KvD"),o=e("L42u").set,i=n.MutationObserver||n.WebKitMutationObserver,c=n.process,a=n.Promise,u="process"==e("R9M2")(c);t.exports=function(){var t,r,e,s=function(){var n,o;for(u&&(n=c.domain)&&n.exit();t;){o=t.fn,t=t.next;try{o()}catch(n){throw t?e():r=void 0,n}}r=void 0,n&&n.enter()};if(u)e=function(){c.nextTick(s)};else if(!i||n.navigator&&n.navigator.standalone)if(a&&a.resolve){var f=a.resolve(void 0);e=function(){f.then(s)}}else e=function(){o.call(n,s)};else{var l=!0,h=document.createTextNode("");new i(s).observe(h,{characterData:!0}),e=function(){h.data=l=!l}}return function(n){var o={fn:n,next:void 0};r&&(r.next=o),t||(t=o,e()),r=o}}},CXw9:function(t,r,e){"use strict";var n,o,i,c,a=e("O4g8"),u=e("7KvD"),s=e("+ZMJ"),f=e("RY/4"),l=e("kM2E"),h=e("EqjI"),v=e("lOnJ"),p=e("2KxR"),d=e("NWt+"),y=e("t8x9"),m=e("L42u").set,g=e("82Mu")(),x=e("qARP"),w=e("dNDb"),_=e("iUbK"),b=e("fJUb"),j=u.TypeError,E=u.process,P=E&&E.versions,L=P&&P.v8||"",F=u.Promise,R="process"==f(E),k=function(){},O=o=x.f,M=!!function(){try{var t=F.resolve(1),r=(t.constructor={})[e("dSzd")("species")]=function(t){t(k,k)};return(R||"function"==typeof PromiseRejectionEvent)&&t.then(k)instanceof r&&0!==L.indexOf("6.6")&&-1===_.indexOf("Chrome/66")}catch(t){}}(),S=function(t){var r;return!(!h(t)||"function"!=typeof(r=t.then))&&r},N=function(t,r){if(!t._n){t._n=!0;var e=t._c;g(function(){for(var n=t._v,o=1==t._s,i=0,c=function(r){var e,i,c,a=o?r.ok:r.fail,u=r.resolve,s=r.reject,f=r.domain;try{a?(o||(2==t._h&&K(t),t._h=1),!0===a?e=n:(f&&f.enter(),e=a(n),f&&(f.exit(),c=!0)),e===r.promise?s(j("Promise-chain cycle")):(i=S(e))?i.call(e,u,s):u(e)):s(n)}catch(t){f&&!c&&f.exit(),s(t)}};e.length>i;)c(e[i++]);t._c=[],t._n=!1,r&&!t._h&&D(t)})}},D=function(t){m.call(u,function(){var r,e,n,o=t._v,i=T(t);if(i&&(r=w(function(){R?E.emit("unhandledRejection",o,t):(e=u.onunhandledrejection)?e({promise:t,reason:o}):(n=u.console)&&n.error&&n.error("Unhandled promise rejection",o)}),t._h=R||T(t)?2:1),t._a=void 0,i&&r.e)throw r.v})},T=function(t){return 1!==t._h&&0===(t._a||t._c).length},K=function(t){m.call(u,function(){var r;R?E.emit("rejectionHandled",t):(r=u.onrejectionhandled)&&r({promise:t,reason:t._v})})},C=function(t){var r=this;r._d||(r._d=!0,(r=r._w||r)._v=t,r._s=2,r._a||(r._a=r._c.slice()),N(r,!0))},J=function(t){var r,e=this;if(!e._d){e._d=!0,e=e._w||e;try{if(e===t)throw j("Promise can't be resolved itself");(r=S(t))?g(function(){var n={_w:e,_d:!1};try{r.call(t,s(J,n,1),s(C,n,1))}catch(t){C.call(n,t)}}):(e._v=t,e._s=1,N(e,!1))}catch(t){C.call({_w:e,_d:!1},t)}}};M||(F=function(t){p(this,F,"Promise","_h"),v(t),n.call(this);try{t(s(J,this,1),s(C,this,1))}catch(t){C.call(this,t)}},(n=function(t){this._c=[],this._a=void 0,this._s=0,this._d=!1,this._v=void 0,this._h=0,this._n=!1}).prototype=e("xH/j")(F.prototype,{then:function(t,r){var e=O(y(this,F));return e.ok="function"!=typeof t||t,e.fail="function"==typeof r&&r,e.domain=R?E.domain:void 0,this._c.push(e),this._a&&this._a.push(e),this._s&&N(this,!1),e.promise},catch:function(t){return this.then(void 0,t)}}),i=function(){var t=new n;this.promise=t,this.resolve=s(J,t,1),this.reject=s(C,t,1)},x.f=O=function(t){return t===F||t===c?new i(t):o(t)}),l(l.G+l.W+l.F*!M,{Promise:F}),e("e6n0")(F,"Promise"),e("bRrM")("Promise"),c=e("FeBl").Promise,l(l.S+l.F*!M,"Promise",{reject:function(t){var r=O(this);return(0,r.reject)(t),r.promise}}),l(l.S+l.F*(a||!M),"Promise",{resolve:function(t){return b(a&&this===c?F:this,t)}}),l(l.S+l.F*!(M&&e("dY0y")(function(t){F.all(t).catch(k)})),"Promise",{all:function(t){var r=this,e=O(r),n=e.resolve,o=e.reject,i=w(function(){var e=[],i=0,c=1;d(t,!1,function(t){var a=i++,u=!1;e.push(void 0),c++,r.resolve(t).then(function(t){u||(u=!0,e[a]=t,--c||n(e))},o)}),--c||n(e)});return i.e&&o(i.v),e.promise},race:function(t){var r=this,e=O(r),n=e.reject,o=w(function(){d(t,!1,function(t){r.resolve(t).then(e.resolve,n)})});return o.e&&n(o.v),e.promise}})},DZOf:function(t,r,e){"use strict";e.d(r,"a",function(){return p}),e.d(r,"b",function(){return d});var n,o,i=e("mvHQ"),c=e.n(i),a=e("Xxa5"),u=e.n(a),s=e("exGp"),f=e.n(s),l=e("mtWM"),h=e.n(l),v="http://116.62.46.96:3000",p=(n=f()(u.a.mark(function t(r){var e;return u.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,h.a.get(v+r);case 2:return e=t.sent,t.abrupt("return",e.data);case 4:case"end":return t.stop()}},t,this)})),function(t){return n.apply(this,arguments)}),d=(o=f()(u.a.mark(function t(r){var e,n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:void 0;return u.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,h.a.post(v+r,c()(n));case 2:return e=t.sent,t.abrupt("return",e.data);case 4:case"end":return t.stop()}},t,this)})),function(t){return o.apply(this,arguments)})},EqBC:function(t,r,e){"use strict";var n=e("kM2E"),o=e("FeBl"),i=e("7KvD"),c=e("t8x9"),a=e("fJUb");n(n.P+n.R,"Promise",{finally:function(t){var r=c(this,o.Promise||i.Promise),e="function"==typeof t;return this.then(e?function(e){return a(r,t()).then(function(){return e})}:t,e?function(e){return a(r,t()).then(function(){throw e})}:t)}})},L42u:function(t,r,e){var n,o,i,c=e("+ZMJ"),a=e("knuC"),u=e("RPLV"),s=e("ON07"),f=e("7KvD"),l=f.process,h=f.setImmediate,v=f.clearImmediate,p=f.MessageChannel,d=f.Dispatch,y=0,m={},g=function(){var t=+this;if(m.hasOwnProperty(t)){var r=m[t];delete m[t],r()}},x=function(t){g.call(t.data)};h&&v||(h=function(t){for(var r=[],e=1;arguments.length>e;)r.push(arguments[e++]);return m[++y]=function(){a("function"==typeof t?t:Function(t),r)},n(y),y},v=function(t){delete m[t]},"process"==e("R9M2")(l)?n=function(t){l.nextTick(c(g,t,1))}:d&&d.now?n=function(t){d.now(c(g,t,1))}:p?(i=(o=new p).port2,o.port1.onmessage=x,n=c(i.postMessage,i,1)):f.addEventListener&&"function"==typeof postMessage&&!f.importScripts?(n=function(t){f.postMessage(t+"","*")},f.addEventListener("message",x,!1)):n="onreadystatechange"in s("script")?function(t){u.appendChild(s("script")).onreadystatechange=function(){u.removeChild(this),g.call(t)}}:function(t){setTimeout(c(g,t,1),0)}),t.exports={set:h,clear:v}},Mhyx:function(t,r,e){var n=e("/bQp"),o=e("dSzd")("iterator"),i=Array.prototype;t.exports=function(t){return void 0!==t&&(n.Array===t||i[o]===t)}},"NWt+":function(t,r,e){var n=e("+ZMJ"),o=e("msXi"),i=e("Mhyx"),c=e("77Pl"),a=e("QRG4"),u=e("3fs2"),s={},f={};(r=t.exports=function(t,r,e,l,h){var v,p,d,y,m=h?function(){return t}:u(t),g=n(e,l,r?2:1),x=0;if("function"!=typeof m)throw TypeError(t+" is not iterable!");if(i(m)){for(v=a(t.length);v>x;x++)if((y=r?g(c(p=t[x])[0],p[1]):g(t[x]))===s||y===f)return y}else for(d=m.call(t);!(p=d.next()).done;)if((y=o(d,g,p.value,r))===s||y===f)return y}).BREAK=s,r.RETURN=f},"RY/4":function(t,r,e){var n=e("R9M2"),o=e("dSzd")("toStringTag"),i="Arguments"==n(function(){return arguments}());t.exports=function(t){var r,e,c;return void 0===t?"Undefined":null===t?"Null":"string"==typeof(e=function(t,r){try{return t[r]}catch(t){}}(r=Object(t),o))?e:i?n(r):"Object"==(c=n(r))&&"function"==typeof r.callee?"Arguments":c}},SldL:function(t,r){!function(r){"use strict";var e,n=Object.prototype,o=n.hasOwnProperty,i="function"==typeof Symbol?Symbol:{},c=i.iterator||"@@iterator",a=i.asyncIterator||"@@asyncIterator",u=i.toStringTag||"@@toStringTag",s="object"==typeof t,f=r.regeneratorRuntime;if(f)s&&(t.exports=f);else{(f=r.regeneratorRuntime=s?t.exports:{}).wrap=w;var l="suspendedStart",h="suspendedYield",v="executing",p="completed",d={},y={};y[c]=function(){return this};var m=Object.getPrototypeOf,g=m&&m(m(M([])));g&&g!==n&&o.call(g,c)&&(y=g);var x=E.prototype=b.prototype=Object.create(y);j.prototype=x.constructor=E,E.constructor=j,E[u]=j.displayName="GeneratorFunction",f.isGeneratorFunction=function(t){var r="function"==typeof t&&t.constructor;return!!r&&(r===j||"GeneratorFunction"===(r.displayName||r.name))},f.mark=function(t){return Object.setPrototypeOf?Object.setPrototypeOf(t,E):(t.__proto__=E,u in t||(t[u]="GeneratorFunction")),t.prototype=Object.create(x),t},f.awrap=function(t){return{__await:t}},P(L.prototype),L.prototype[a]=function(){return this},f.AsyncIterator=L,f.async=function(t,r,e,n){var o=new L(w(t,r,e,n));return f.isGeneratorFunction(r)?o:o.next().then(function(t){return t.done?t.value:o.next()})},P(x),x[u]="Generator",x[c]=function(){return this},x.toString=function(){return"[object Generator]"},f.keys=function(t){var r=[];for(var e in t)r.push(e);return r.reverse(),function e(){for(;r.length;){var n=r.pop();if(n in t)return e.value=n,e.done=!1,e}return e.done=!0,e}},f.values=M,O.prototype={constructor:O,reset:function(t){if(this.prev=0,this.next=0,this.sent=this._sent=e,this.done=!1,this.delegate=null,this.method="next",this.arg=e,this.tryEntries.forEach(k),!t)for(var r in this)"t"===r.charAt(0)&&o.call(this,r)&&!isNaN(+r.slice(1))&&(this[r]=e)},stop:function(){this.done=!0;var t=this.tryEntries[0].completion;if("throw"===t.type)throw t.arg;return this.rval},dispatchException:function(t){if(this.done)throw t;var r=this;function n(n,o){return a.type="throw",a.arg=t,r.next=n,o&&(r.method="next",r.arg=e),!!o}for(var i=this.tryEntries.length-1;i>=0;--i){var c=this.tryEntries[i],a=c.completion;if("root"===c.tryLoc)return n("end");if(c.tryLoc<=this.prev){var u=o.call(c,"catchLoc"),s=o.call(c,"finallyLoc");if(u&&s){if(this.prev<c.catchLoc)return n(c.catchLoc,!0);if(this.prev<c.finallyLoc)return n(c.finallyLoc)}else if(u){if(this.prev<c.catchLoc)return n(c.catchLoc,!0)}else{if(!s)throw new Error("try statement without catch or finally");if(this.prev<c.finallyLoc)return n(c.finallyLoc)}}}},abrupt:function(t,r){for(var e=this.tryEntries.length-1;e>=0;--e){var n=this.tryEntries[e];if(n.tryLoc<=this.prev&&o.call(n,"finallyLoc")&&this.prev<n.finallyLoc){var i=n;break}}i&&("break"===t||"continue"===t)&&i.tryLoc<=r&&r<=i.finallyLoc&&(i=null);var c=i?i.completion:{};return c.type=t,c.arg=r,i?(this.method="next",this.next=i.finallyLoc,d):this.complete(c)},complete:function(t,r){if("throw"===t.type)throw t.arg;return"break"===t.type||"continue"===t.type?this.next=t.arg:"return"===t.type?(this.rval=this.arg=t.arg,this.method="return",this.next="end"):"normal"===t.type&&r&&(this.next=r),d},finish:function(t){for(var r=this.tryEntries.length-1;r>=0;--r){var e=this.tryEntries[r];if(e.finallyLoc===t)return this.complete(e.completion,e.afterLoc),k(e),d}},catch:function(t){for(var r=this.tryEntries.length-1;r>=0;--r){var e=this.tryEntries[r];if(e.tryLoc===t){var n=e.completion;if("throw"===n.type){var o=n.arg;k(e)}return o}}throw new Error("illegal catch attempt")},delegateYield:function(t,r,n){return this.delegate={iterator:M(t),resultName:r,nextLoc:n},"next"===this.method&&(this.arg=e),d}}}function w(t,r,e,n){var o=r&&r.prototype instanceof b?r:b,i=Object.create(o.prototype),c=new O(n||[]);return i._invoke=function(t,r,e){var n=l;return function(o,i){if(n===v)throw new Error("Generator is already running");if(n===p){if("throw"===o)throw i;return S()}for(e.method=o,e.arg=i;;){var c=e.delegate;if(c){var a=F(c,e);if(a){if(a===d)continue;return a}}if("next"===e.method)e.sent=e._sent=e.arg;else if("throw"===e.method){if(n===l)throw n=p,e.arg;e.dispatchException(e.arg)}else"return"===e.method&&e.abrupt("return",e.arg);n=v;var u=_(t,r,e);if("normal"===u.type){if(n=e.done?p:h,u.arg===d)continue;return{value:u.arg,done:e.done}}"throw"===u.type&&(n=p,e.method="throw",e.arg=u.arg)}}}(t,e,c),i}function _(t,r,e){try{return{type:"normal",arg:t.call(r,e)}}catch(t){return{type:"throw",arg:t}}}function b(){}function j(){}function E(){}function P(t){["next","throw","return"].forEach(function(r){t[r]=function(t){return this._invoke(r,t)}})}function L(t){var r;this._invoke=function(e,n){function i(){return new Promise(function(r,i){!function r(e,n,i,c){var a=_(t[e],t,n);if("throw"!==a.type){var u=a.arg,s=u.value;return s&&"object"==typeof s&&o.call(s,"__await")?Promise.resolve(s.__await).then(function(t){r("next",t,i,c)},function(t){r("throw",t,i,c)}):Promise.resolve(s).then(function(t){u.value=t,i(u)},c)}c(a.arg)}(e,n,r,i)})}return r=r?r.then(i,i):i()}}function F(t,r){var n=t.iterator[r.method];if(n===e){if(r.delegate=null,"throw"===r.method){if(t.iterator.return&&(r.method="return",r.arg=e,F(t,r),"throw"===r.method))return d;r.method="throw",r.arg=new TypeError("The iterator does not provide a 'throw' method")}return d}var o=_(n,t.iterator,r.arg);if("throw"===o.type)return r.method="throw",r.arg=o.arg,r.delegate=null,d;var i=o.arg;return i?i.done?(r[t.resultName]=i.value,r.next=t.nextLoc,"return"!==r.method&&(r.method="next",r.arg=e),r.delegate=null,d):i:(r.method="throw",r.arg=new TypeError("iterator result is not an object"),r.delegate=null,d)}function R(t){var r={tryLoc:t[0]};1 in t&&(r.catchLoc=t[1]),2 in t&&(r.finallyLoc=t[2],r.afterLoc=t[3]),this.tryEntries.push(r)}function k(t){var r=t.completion||{};r.type="normal",delete r.arg,t.completion=r}function O(t){this.tryEntries=[{tryLoc:"root"}],t.forEach(R,this),this.reset(!0)}function M(t){if(t){var r=t[c];if(r)return r.call(t);if("function"==typeof t.next)return t;if(!isNaN(t.length)){var n=-1,i=function r(){for(;++n<t.length;)if(o.call(t,n))return r.value=t[n],r.done=!1,r;return r.value=e,r.done=!0,r};return i.next=i}}return{next:S}}function S(){return{value:e,done:!0}}}(function(){return this}()||Function("return this")())},TVmP:function(t,r,e){"use strict";var n={render:function(){var t=this.$createElement,r=this._self._c||t;return r("div",{staticClass:"footer",attrs:{id:"Footer"}},[r("el-row",[r("el-col",{attrs:{span:8}},[r("router-link",{attrs:{to:"/task"}},[r("el-button",{staticStyle:{"background-color":"#D9F9FF"},attrs:{circle:""}},[this._v(" 任务")])],1)],1),this._v(" "),r("el-col",{attrs:{span:8}},[r("router-link",{attrs:{to:"/square"}},[r("el-button",{staticStyle:{"background-color":"#D9F9FF"},attrs:{circle:""}},[this._v(" 广场")])],1)],1),this._v(" "),r("el-col",{attrs:{span:8}},[r("router-link",{attrs:{to:"/myindex"}},[r("el-button",{staticStyle:{"background-color":"#D9F9FF"},attrs:{circle:""}},[this._v("我的")])],1)],1)],1)],1)},staticRenderFns:[]};var o=e("VU/8")({name:"Footer",data:function(){return{}},methods:{}},n,!1,function(t){e("bItC")},null,null);r.a=o.exports},U5ju:function(t,r,e){e("M6a0"),e("zQR9"),e("+tPU"),e("CXw9"),e("EqBC"),e("jKW+"),t.exports=e("FeBl").Promise},"Ui/T":function(t,r,e){"use strict";e.d(r,"a",function(){return s});var n,o=e("Xxa5"),i=e.n(o),c=e("exGp"),a=e.n(c),u=e("DZOf"),s=(n=a()(i.a.mark(function t(){var r;return i.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,Object(u.a)("/api/user/info");case 2:return r=t.sent,console.log(r),t.abrupt("return",r);case 5:case"end":return t.stop()}},t,this)})),function(){return n.apply(this,arguments)})},Xxa5:function(t,r,e){t.exports=e("jyFz")},bItC:function(t,r){},bRrM:function(t,r,e){"use strict";var n=e("7KvD"),o=e("FeBl"),i=e("evD5"),c=e("+E39"),a=e("dSzd")("species");t.exports=function(t){var r="function"==typeof o[t]?o[t]:n[t];c&&r&&!r[a]&&i.f(r,a,{configurable:!0,get:function(){return this}})}},dNDb:function(t,r){t.exports=function(t){try{return{e:!1,v:t()}}catch(t){return{e:!0,v:t}}}},dY0y:function(t,r,e){var n=e("dSzd")("iterator"),o=!1;try{var i=[7][n]();i.return=function(){o=!0},Array.from(i,function(){throw 2})}catch(t){}t.exports=function(t,r){if(!r&&!o)return!1;var e=!1;try{var i=[7],c=i[n]();c.next=function(){return{done:e=!0}},i[n]=function(){return c},t(i)}catch(t){}return e}},exGp:function(t,r,e){"use strict";r.__esModule=!0;var n,o=e("//Fk"),i=(n=o)&&n.__esModule?n:{default:n};r.default=function(t){return function(){var r=t.apply(this,arguments);return new i.default(function(t,e){return function n(o,c){try{var a=r[o](c),u=a.value}catch(t){return void e(t)}if(!a.done)return i.default.resolve(u).then(function(t){n("next",t)},function(t){n("throw",t)});t(u)}("next")})}}},fJUb:function(t,r,e){var n=e("77Pl"),o=e("EqjI"),i=e("qARP");t.exports=function(t,r){if(n(t),o(r)&&r.constructor===t)return r;var e=i.f(t);return(0,e.resolve)(r),e.promise}},iUbK:function(t,r,e){var n=e("7KvD").navigator;t.exports=n&&n.userAgent||""},iyCB:function(t,r,e){t.exports=e.p+"static/img/test_1.83965ee.jpg"},"jKW+":function(t,r,e){"use strict";var n=e("kM2E"),o=e("qARP"),i=e("dNDb");n(n.S,"Promise",{try:function(t){var r=o.f(this),e=i(t);return(e.e?r.reject:r.resolve)(e.v),r.promise}})},jyFz:function(t,r,e){var n=function(){return this}()||Function("return this")(),o=n.regeneratorRuntime&&Object.getOwnPropertyNames(n).indexOf("regeneratorRuntime")>=0,i=o&&n.regeneratorRuntime;if(n.regeneratorRuntime=void 0,t.exports=e("SldL"),o)n.regeneratorRuntime=i;else try{delete n.regeneratorRuntime}catch(t){n.regeneratorRuntime=void 0}},knuC:function(t,r){t.exports=function(t,r,e){var n=void 0===e;switch(r.length){case 0:return n?t():t.call(e);case 1:return n?t(r[0]):t.call(e,r[0]);case 2:return n?t(r[0],r[1]):t.call(e,r[0],r[1]);case 3:return n?t(r[0],r[1],r[2]):t.call(e,r[0],r[1],r[2]);case 4:return n?t(r[0],r[1],r[2],r[3]):t.call(e,r[0],r[1],r[2],r[3])}return t.apply(e,r)}},msXi:function(t,r,e){var n=e("77Pl");t.exports=function(t,r,e,o){try{return o?r(n(e)[0],e[1]):r(e)}catch(r){var i=t.return;throw void 0!==i&&n(i.call(t)),r}}},mvHQ:function(t,r,e){t.exports={default:e("qkKv"),__esModule:!0}},qARP:function(t,r,e){"use strict";var n=e("lOnJ");t.exports.f=function(t){return new function(t){var r,e;this.promise=new t(function(t,n){if(void 0!==r||void 0!==e)throw TypeError("Bad Promise constructor");r=t,e=n}),this.resolve=n(r),this.reject=n(e)}(t)}},qkKv:function(t,r,e){var n=e("FeBl"),o=n.JSON||(n.JSON={stringify:JSON.stringify});t.exports=function(t){return o.stringify.apply(o,arguments)}},t8x9:function(t,r,e){var n=e("77Pl"),o=e("lOnJ"),i=e("dSzd")("species");t.exports=function(t,r){var e,c=n(t).constructor;return void 0===c||void 0==(e=n(c)[i])?r:o(e)}},"xH/j":function(t,r,e){var n=e("hJx8");t.exports=function(t,r,e){for(var o in r)e&&t[o]?t[o]=r[o]:n(t,o,r[o]);return t}}});
//# sourceMappingURL=0.3927d00cb74ab8ebf7b6.js.map