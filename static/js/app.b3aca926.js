(function(t){function e(e){for(var a,i,o=e[0],l=e[1],c=e[2],u=0,d=[];u<o.length;u++)i=o[u],Object.prototype.hasOwnProperty.call(r,i)&&r[i]&&d.push(r[i][0]),r[i]=0;for(a in l)Object.prototype.hasOwnProperty.call(l,a)&&(t[a]=l[a]);f&&f(e);while(d.length)d.shift()();return s.push.apply(s,c||[]),n()}function n(){for(var t,e=0;e<s.length;e++){for(var n=s[e],a=!0,i=1;i<n.length;i++){var o=n[i];0!==r[o]&&(a=!1)}a&&(s.splice(e--,1),t=l(l.s=n[0]))}return t}var a={},i={app:0},r={app:0},s=[];function o(t){return l.p+"js/"+({dict:"dict",settings:"settings"}[t]||t)+"."+{dict:"33562b15",settings:"49501d03"}[t]+".js"}function l(e){if(a[e])return a[e].exports;var n=a[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,l),n.l=!0,n.exports}l.e=function(t){var e=[],n={dict:1};i[t]?e.push(i[t]):0!==i[t]&&n[t]&&e.push(i[t]=new Promise((function(e,n){for(var a="css/"+({dict:"dict",settings:"settings"}[t]||t)+"."+{dict:"5d342184",settings:"31d6cfe0"}[t]+".css",r=l.p+a,s=document.getElementsByTagName("link"),o=0;o<s.length;o++){var c=s[o],u=c.getAttribute("data-href")||c.getAttribute("href");if("stylesheet"===c.rel&&(u===a||u===r))return e()}var d=document.getElementsByTagName("style");for(o=0;o<d.length;o++){c=d[o],u=c.getAttribute("data-href");if(u===a||u===r)return e()}var f=document.createElement("link");f.rel="stylesheet",f.type="text/css",f.onload=e,f.onerror=function(e){var a=e&&e.target&&e.target.src||r,s=new Error("Loading CSS chunk "+t+" failed.\n("+a+")");s.code="CSS_CHUNK_LOAD_FAILED",s.request=a,delete i[t],f.parentNode.removeChild(f),n(s)},f.href=r;var m=document.getElementsByTagName("head")[0];m.appendChild(f)})).then((function(){i[t]=0})));var a=r[t];if(0!==a)if(a)e.push(a[2]);else{var s=new Promise((function(e,n){a=r[t]=[e,n]}));e.push(a[2]=s);var c,u=document.createElement("script");u.charset="utf-8",u.timeout=120,l.nc&&u.setAttribute("nonce",l.nc),u.src=o(t);var d=new Error;c=function(e){u.onerror=u.onload=null,clearTimeout(f);var n=r[t];if(0!==n){if(n){var a=e&&("load"===e.type?"missing":e.type),i=e&&e.target&&e.target.src;d.message="Loading chunk "+t+" failed.\n("+a+": "+i+")",d.name="ChunkLoadError",d.type=a,d.request=i,n[1](d)}r[t]=void 0}};var f=setTimeout((function(){c({type:"timeout",target:u})}),12e4);u.onerror=u.onload=c,document.head.appendChild(u)}return Promise.all(e)},l.m=t,l.c=a,l.d=function(t,e,n){l.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},l.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},l.t=function(t,e){if(1&e&&(t=l(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(l.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)l.d(n,a,function(e){return t[e]}.bind(null,a));return n},l.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return l.d(e,"a",e),e},l.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},l.p="/",l.oe=function(t){throw console.error(t),t};var c=window["webpackJsonp"]=window["webpackJsonp"]||[],u=c.push.bind(c);c.push=e,c=c.slice();for(var d=0;d<c.length;d++)e(c[d]);var f=u;s.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},1352:function(t,e,n){},"43b3":function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("nav",{staticClass:"navbar navbar-expand-lg navbar-light bg-light ps-2"},[n("div",{staticClass:"container-fluid"},[t.showBackBtn?n("div",[n("button",{staticClass:"btn btn-primary",on:{click:function(e){return t.$router.go(-1)}}},[t._v("Назад")])]):t._e(),n("span",{staticClass:"navbar-brand mb-0 me-auto",class:{"ms-4":t.showBackBtn}},[t._v(" "+t._s(t.title)+" ")])])])])},i=[],r=(n("7db0"),n("d3b7"),{props:["title","exim","back"],computed:{showBackBtn:function(){var t=this;return"true"==this.back&&!this.$store.getters.sidebarItems.find((function(e){return e.title==t.title}))}}}),s=r,o=n("2877"),l=Object(o["a"])(s,a,i,!1,null,null,null);e["a"]=l.exports},"54c2":function(t,e,n){"use strict";n.d(e,"a",(function(){return u}));var a=n("1da1"),i=n("d4ec"),r=n("bee2"),s=(n("96cf"),n("99af"),n("b64b"),n("d3b7"),n("3ca3"),n("ddb0"),n("2b3d"),n("9861"),n("bc3a")),o=n.n(s),l=n("2b0e"),c=n("51c2");l["default"].use(c["a"]);var u=function(){function t(){Object(i["a"])(this,t),this.api="http://localhost:".concat("1337","/api"),this.version="v0.1";var e=new l["default"];this.showErrorToast=function(t){console.log(t),e.$bvToast.toast("Произошла ошибка при загрузке данных!",{title:"Ошибка",autoHideDelay:5e3,variant:"danger"})}}return Object(r["a"])(t,[{key:"getSidebarItems",value:function(){var t=this,e=o.a.get("".concat(this.api,"/").concat(this.version,"/sidebar")),n=e.then((function(t){return t.data})).catch((function(e){return t.showErrorToast(e)}));return n}},{key:"getData",value:function(t){var e=this,n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};0!=Object.keys(n).length&&console.info("[getData() params]",n);var a=o.a.get("".concat(this.api,"/").concat(this.version,"/get/").concat(t),{params:n}),i=a.then((function(t){return t.data})).catch((function(t){return e.showErrorToast(t)}));return i}},{key:"getTableInfo",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){var n,a=this;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,o.a.get("".concat(this.api,"/").concat(this.version,"/get_dict/").concat(e)).catch((function(t){return a.showErrorToast(t)}));case 2:return n=t.sent,t.abrupt("return",n.data);case 4:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"getTablesInfo",value:function(){var t=this,e=o.a.get("".concat(this.api,"/").concat(this.version,"/get_dict")),n=e.then((function(t){return t.data})).catch((function(e){return t.showErrorToast(e)}));return n}},{key:"updateField",value:function(t,e,n){var a=this,i=o.a.put("".concat(this.api,"/").concat(this.version,"/update/").concat(t,"/").concat(e),n),r=i.then((function(t){return t.data})).catch((function(t){return a.showErrorToast(t)}));return r}},{key:"addRow",value:function(t,e){var n=this;console.log("[addRow() params]",t,e);var a=o.a.post("".concat(this.api,"/").concat(this.version,"/add/").concat(t),e),i=a.then((function(t){return t.data})).catch((function(t){return n.showErrorToast(t)}));return i}},{key:"deleteRow",value:function(t,e){var n=this,a=o.a.delete("".concat(this.api,"/").concat(this.version,"/delete/").concat(t,"/").concat(e)),i=a.then((function(t){return t.data})).catch((function(t){return n.showErrorToast(t)}));return i}},{key:"getEstimateInfo",value:function(){var t=this,e=o.a.get("".concat(this.api,"/").concat(this.version,"/get_estimate_records")),n=e.then((function(t){return t.data})).catch((function(e){return t.showErrorToast(e)}));return n}},{key:"addEstimate",value:function(t){var e=this,n=o.a.post("".concat(this.api,"/").concat(this.version,"/calculate_estimate"),t),a=n.then((function(t){return t.data})).catch((function(t){return e.showErrorToast(t)}));return a}},{key:"importTable",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e,n){var a,i,r=this;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return a=new FormData,a.append("file",n),t.next=4,o.a.post("".concat(this.api,"/").concat(this.version,"/import/").concat(e),a,{headers:{"Content-Type":"multipart/form-data"}}).catch((function(t){return r.showErrorToast(t)}));case 4:return i=t.sent,t.abrupt("return",i.data);case 6:case"end":return t.stop()}}),t,this)})));function e(e,n){return t.apply(this,arguments)}return e}()},{key:"exportTable",value:function(t){o()({url:"".concat(this.api,"/").concat(this.version,"/export/").concat(t),method:"GET",responseType:"blob"}).then((function(e){var n=window.URL.createObjectURL(new Blob([e.data])),a=document.createElement("a");a.href=n,a.setAttribute(t,"file.xlsx"),a.click(),window.URL.revokeObjectURL(n)}))}}]),t}()},"56d7":function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var a=n("2b0e"),i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{ref:"root",staticClass:"d-flex",attrs:{id:"app"}},[n("side-bar",{attrs:{items:t.sidebarItems}}),n("div",{staticClass:"d-flex flex-column w-100"},[n("router-view")],1)],1)},r=[],s=n("2f62"),o=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"d-flex flex-column flex-shrink-0 p-3 bg-light vh-100",staticStyle:{width:"280px"}},[n("a",{staticClass:"d-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none",attrs:{href:"/"}},[n("b-iconstack",{staticClass:"me-3",attrs:{"font-scale":"2"}},[n("b-icon",{attrs:{stacked:"",icon:"gear-wide",scale:"1.5"}}),n("b-icon",{attrs:{stacked:"",icon:"wrench",scale:"0.75","flip-h":""}}),n("b-icon",{attrs:{stacked:"",icon:"hammer",scale:"0.75"}})],1),n("span",{staticClass:"fs-4"},[t._v("Automation Build")])],1),n("hr"),n("ul",{staticClass:"nav nav-pills flex-column"},[n("li",{staticClass:"nav-item"},[n("router-link",{staticClass:"nav-link link-dark",attrs:{to:"/","exact-active-class":"active"}},[n("b-icon",{staticClass:"me-1",attrs:{icon:"calculator",variant:"dark"}}),t._v(" Расчет ")],1)],1)]),n("hr"),n("ul",{staticClass:"nav nav-pills flex-column mb-auto"},t._l(t.items,(function(e){return n("li",{key:e.id},[n("router-link",{staticClass:"nav-link link-dark",attrs:{to:{name:"dict",params:{name:e.name}},"exact-active-class":"active"}},[n("b-icon",{staticClass:"me-1",attrs:{icon:e.icon,variant:"dark"}}),t._v(" "+t._s(e.title)+" ")],1)],1)})),0),n("hr"),n("ul",{staticClass:"nav nav-pills flex-column"},[n("li",[n("router-link",{staticClass:"nav-link link-dark",attrs:{to:"/settings","exact-active-class":"active"}},[n("b-icon",{staticClass:"me-1",attrs:{icon:"gear",variant:"dark"}}),t._v(" Настройки ")],1)],1)])])},l=[],c={props:["items"]},u=c,d=n("2877"),f=Object(d["a"])(u,o,l,!1,null,null,null),m=f.exports,b={components:{SideBar:m},computed:Object(s["c"])(["sidebarItems"]),methods:Object(s["b"])(["fetchSidebarItems"]),mounted:function(){this.fetchSidebarItems()}},p=b,h=Object(d["a"])(p,i,r,!1,null,null,null),g=h.exports,v=(n("d3b7"),n("3ca3"),n("ddb0"),n("8c4f")),k=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("Title",{attrs:{title:t.title,back:"false"}}),n("b-container",{staticClass:"p-4",attrs:{fluid:""}},[n("b-row",[n("b-col",{attrs:{cols:"12",xl:"8"}},[t.isEditing?t._e():n("EstimatesTable",{on:{toggleEditingView:t.onToggleView}}),t.isEditing?n("EstimateForm",{attrs:{id:t.editingId},on:{toggleEditingView:t.onToggleView}}):t._e(),t.isEditing?t._e():n("b-button",{attrs:{variant:"primary"},on:{click:function(e){t.isEditing=!0}}},[t._v(" Добавить ")])],1)],1)],1)],1)},w=[],y=n("43b3"),_=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("search-bar",{attrs:{filter:t.searchFilter},on:{filterChange:t.onFilterChange}}),n("b-table",{staticClass:"text-nowrap",attrs:{bordered:"",responsive:"","show-empty":"",id:"table",fields:t.fields,items:t.items,filter:t.searchFilter},scopedSlots:t._u([{key:"cell(actions)",fn:function(e){return[n("b-button",{staticClass:"mr-2",attrs:{variant:"success"},on:{click:function(n){return t.exportToExcel(e.item.id)}}},[t._v(" Выгрузить в Excel ")]),n("b-button",{on:{click:e.toggleDetails}},[t._v(" Подробнее "+t._s(e.detailsShowing?"↑":"↓")+" ")])]}},{key:"table-busy",fn:function(){return[n("div",{staticClass:"text-center my-2"},[n("b-spinner",{staticClass:"align-middle me-2"}),n("strong",[t._v("Загрузка...")])],1)]},proxy:!0},{key:"row-details",fn:function(e){return[n("b-row",{staticClass:"mb-2"},[n("b-col",[n("b",[t._v("Цена заказчика:")]),t._v(" "+t._s(e.item.id))]),n("b-col",{staticClass:"text-right"},[n("b-button",{staticClass:"mr-2"},[t._v("Материалы")]),n("b-button",{staticClass:"mr-2"},[t._v("Работы")]),n("b-button",{attrs:{variant:"info"}},[t._v("Редактировать")])],1)],1)]}}])})],1)},j=[],x=n("1da1"),T=n("5530"),F=(n("96cf"),n("688b")),O={components:{SearchBar:F["a"]},data:function(){return{searchFilter:null,fields:[{key:"name",label:"Наименование"},{key:"actions",label:"Действия"}],items:[{id:-1,name:"ХАРДКОД"}]}},computed:Object(T["a"])({},Object(s["c"])(["estimatesList"])),methods:Object(T["a"])(Object(T["a"])({},Object(s["b"])(["loadEstimateInfo"])),{},{init:function(){var t=this;return Object(x["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:t.loadEstimateInfo();case 1:case"end":return e.stop()}}),e)})))()},onFilterChange:function(t){this.searchFilter=t},exportToExcel:function(t){console.log("TODO: implement exportToExcel(".concat(t,")"))}}),mounted:function(){this.init()}},E=O,C=Object(d["a"])(E,_,j,!1,null,null,null),I=C.exports,L=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("b-row",{staticClass:"my-2"},[n("b-col",{attrs:{sm:"3"}},[n("label",{attrs:{for:"name-input"}},[t._v("ФИО:")])]),n("b-col",{attrs:{sm:"9"}},[n("b-form-input",{attrs:{id:"name-input",placeholder:"Введите ваше ФИО"},model:{value:t.name,callback:function(e){t.name=e},expression:"name"}})],1)],1),n("b-row",{staticClass:"my-2"},[n("b-col",{attrs:{sm:"3"}},[n("label",{attrs:{for:"name-input"}},[t._v("Проект:")])]),n("b-col",{attrs:{sm:"9"}},[n("change-field-modal",{ref:"project-input",attrs:{label:"Не выбрано",model:"project-input",rowId:"-1",items:t.projectsList},on:{updateField:t.onProjectInputUpdate,labelChange:t.onProjectLabelChange}})],1)],1),n("b-row",{staticClass:"my-2"},[n("b-col",{attrs:{sm:"3"}},[n("label",{attrs:{for:"name-input"}},[t._v("Базовая комплектация:")])]),n("b-col",{attrs:{sm:"9"}},[n("b-form-checkbox",{attrs:{size:"lg"},model:{value:t.isBaseEquipment,callback:function(e){t.isBaseEquipment=e},expression:"isBaseEquipment"}})],1)],1),n("BaseTable",{staticClass:"mb-4",attrs:{showBase:t.isBaseEquipment},on:{updateAdditionalWorks:t.onUpdateAdditionalWorks}}),t.isBaseEquipment?t._e():n("StagesTable",{staticClass:"mb-4",on:{updateWorkTechnologies:t.onUpdateWorkTechnologies}}),n("b-row",{staticClass:"my-2"},[n("b-col",{attrs:{cols:"2"}},[n("b-button",{attrs:{variant:"primary"},on:{click:t.saveEstimate}},[t._v(" Сохранить ")])],1),n("b-col",{staticClass:"text-end"},[n("b-button",{attrs:{variant:"danger"},on:{click:function(e){return t.$emit("toggleEditingView",!1)}}},[t._v(" Отмена ")])],1)],1)],1)},R=[],S=(n("7db0"),n("b0c0"),n("d6cf")),B=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[t.showBase?n("b-card",{staticClass:"mb-4",attrs:{"no-body":"",header:"Базовые работы"}},[n("b-list-group",{attrs:{flush:""}},t._l(t.baseWorksList,(function(e){return n("b-list-group-item",{key:e.id},[t._v(t._s(e.name))])})),1)],1):t._e(),n("b-card",{staticClass:"mb-2",attrs:{"no-body":"",header:"Дополнительные работы"}},[n("b-list-group",{attrs:{flush:""}},t._l(t.notBaseWorksList,(function(e){return n("b-list-group-item",{key:e.id},[n("b-form-checkbox",{attrs:{value:e.id},model:{value:t.selectedAdditionalWorks,callback:function(e){t.selectedAdditionalWorks=e},expression:"selectedAdditionalWorks"}},[t._v(t._s(e.name))])],1)})),1)],1)],1)},M=[],$={props:["showBase"],data:function(){return{selectedAdditionalWorks:[]}},computed:Object(T["a"])({},Object(s["c"])(["worksList","baseWorksList","notBaseWorksList"])),methods:Object(T["a"])(Object(T["a"])({},Object(s["b"])(["loadWorks"])),{},{init:function(){var t=this;return Object(x["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:t.loadWorks({table_name:"work"});case 1:case"end":return e.stop()}}),e)})))()}}),watch:{selectedAdditionalWorks:function(t){this.$emit("updateAdditionalWorks",t)}},mounted:function(){this.init()}},P=$,W=Object(d["a"])(P,B,M,!1,null,null,null),A=W.exports,D=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("b-card",{staticClass:"mb-2",attrs:{"no-body":"",header:"Стадии работ"}},[n("b-list-group",{attrs:{flush:""}},t._l(t.stagesList,(function(e){return n("b-list-group-item",{key:e.id},[n("b-row",[n("b-col",[n("b-form-checkbox",{attrs:{value:e.id},model:{value:t.selectedStages,callback:function(e){t.selectedStages=e},expression:"selectedStages"}},[t._v(t._s(e.name))])],1),n("b-col",{staticClass:"text-end"},[t.selectedStages.includes(e.id)?n("change-field-modal",{ref:"tech-field-"+e.id,refInFor:!0,staticClass:"negative-margin",attrs:{label:"Выберите технологию",model:t.techModel,rowId:e.id,items:t.techList,size:"sm"},on:{updateField:t.onUpdateField}}):t._e()],1)],1)],1)})),1)],1)],1)},U=[],q=(n("4de4"),n("caad"),n("2532"),n("a434"),{components:{ChangeFieldModal:S["a"]},data:function(){return{fields:[{key:"checked",label:" "},{key:"name",label:"Наименование"},{key:"actions",label:" "}],stageModel:"work_stage",selectedStages:[],techModel:"work_technology",selectedWorkTech:[]}},computed:Object(T["a"])({},Object(s["c"])(["stagesList","techList"])),methods:Object(T["a"])(Object(T["a"])({},Object(s["b"])(["loadStages","loadTechList"])),{},{onUpdateField:function(t){var e=t.id,n=t.fields;this.$set(this.selectedWorkTech,e,n.value),this.$refs["tech-field-".concat(e)][0].labelReplacement=this.getFieldById(n.value,this.techModel,"name")},getFieldById:function(t,e,n){return this.techList.find((function(e){return e.id==t}))[n]}}),watch:{selectedWorkTech:function(t){this.$emit("updateWorkTechnologies",t.filter(Boolean))},selectedStages:function(t,e){var n=e.filter((function(e){return!t.includes(e)}));n[0]&&this.selectedWorkTech.splice(n,1)}},mounted:function(){this.loadStages({table_name:this.stageModel}),this.loadTechList({table_name:this.techModel})}}),N=q,V=(n("8f19"),Object(d["a"])(N,D,U,!1,null,"20c8154f",null)),z=V.exports,G={components:{ChangeFieldModal:S["a"],BaseTable:A,StagesTable:z},props:["id"],data:function(){return{name:null,selectedProjectId:null,selectedAdditionalWorks:[],selectedWorkTechnologies:[],isBaseEquipment:!0}},computed:Object(T["a"])({},Object(s["c"])(["projectsList"])),methods:Object(T["a"])(Object(T["a"])({},Object(s["b"])(["loadProjects","addEstimate"])),{},{init:function(){var t=this;return Object(x["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:t.loadProjects({table_name:"project"});case 1:case"end":return e.stop()}}),e)})))()},getFieldById:function(t,e,n){return this.projectsList.find((function(e){return e.id==t}))[n]},onProjectLabelChange:function(t){var e=t.id,n=t.model;this.$refs["project-input"].labelReplacement=this.getFieldById(e,n,"name")},onProjectInputUpdate:function(t){t._id;var e=t.fields;this.selectedProjectId=e.value},onUpdateAdditionalWorks:function(t){this.selectedAdditionalWorks=t},onUpdateWorkTechnologies:function(t){this.selectedWorkTechnologies=t},saveEstimate:function(){var t=Object(T["a"])(Object(T["a"])({client_info:this.name,use_base:this.isBaseEquipment,project_id:this.selectedProjectId},this.selectedAdditionalWorks.length&&{additional_works:this.selectedAdditionalWorks}),this.selectedWorkTechnologies.length&&{work_technologies:this.selectedWorkTechnologies});console.table(t),this.addEstimate({fields:t})}}),mounted:function(){this.init()}},H=G,J=Object(d["a"])(H,L,R,!1,null,null,null),K=J.exports,Q={components:{Title:y["a"],EstimateForm:K,EstimatesTable:I},data:function(){return{title:"Расчеты",isEditing:!1,editingId:null}},computed:{},methods:{onToggleView:function(t){this.isEditing=t}}},X=Q,Y=Object(d["a"])(X,k,w,!1,null,null,null),Z=Y.exports;a["default"].use(v["a"]);var tt=[{path:"/",name:"Расчеты",component:Z},{path:"/dict/:name",name:"dict",props:!0,component:function(){return n.e("dict").then(n.bind(null,"29a8"))}},{path:"/dict/:parent/:name/:id",name:"child-dict",props:!0,component:function(){return n.e("dict").then(n.bind(null,"29a8"))}},{path:"/settings",name:"settings",component:function(){return n.e("settings").then(n.bind(null,"26d3"))}}],et=new v["a"]({mode:"history",base:"/",routes:tt}),nt=et,at=(n("159b"),n("c740"),n("54c2")),it=new at["a"],rt={actions:{getFiltersItems:function(t){var e=t.commit,n=t.state;e("resetFilterList"),n.filters.model.forEach((function(t){it.getData(t.key).then((function(n){e("updateFilterList",{key:[t.key],data:n})}))}))},extendFilters:function(t,e){var n=t.commit,a=t.state;e.forEach((function(t,e){n("updateObj",{obj:a.filters.model[e],key:"disabled",data:0!=e}),n("updateObj",{obj:a.filters.model[e],key:"text",data:"Не выбрано"}),n("updateObj",{obj:a.filters.state,key:[t.key],data:""})}))},resetFiltersFromId:function(t){for(var e=t.commit,n=t.state,a=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0,i=a;i<n.filters.model.length;i++)e("resetFilterLabel",{model:n.filters.model[i].key}),e("updateObj",{obj:n.filters.model[i],key:"disabled",data:i!=a}),e("updateObj",{obj:n.filters.state,key:n.filters.model[i].key,data:""});0==a&&e("updateTableFilterState",!1)},applyFilters:function(t,e){var n=t.commit,a=t.state,i=a.filters.model.findIndex((function(t){return t.key==e.field}));i!=a.filters.model.length-1&&n("updateObj",{obj:a.filters.model[i+1],key:"disabled",data:!1}),n("updateTableFilterState",!0),n("updateObj",{obj:a.filters.state,key:e.field,data:e.value})}},mutations:{resetFilterList:function(t){t.filters.list={}},resetFilters:function(t){t.filters.list={},t.filters.model=[],t.filters.state={}},resetFilterLabel:function(t,e){var n=e.model;t.filters.model.find((function(t){return t.key==n})).text="Не выбрано"},updateFiltersModel:function(t,e){t.filters.model=e},updateFilterList:function(t,e){var n=e.key,a=e.data;this.$app.$set(t.filters.list,n,a)},updateFilterLabel:function(t,e){var n=e.itemId,a=e.model;t.filters.model.find((function(t){return t.key==a})).text=t.filters.list[a].find((function(t){return t.id==n}))["name"]}},state:{filters:{model:[],list:{},state:{}}},getters:{filtersData:function(t){return t.filters},filterParams:function(t){return Object(T["a"])(Object(T["a"])({},t.filters.state),{mode:"advanced_filters"})}}},st=new at["a"],ot={actions:{getTableInfo:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i,r;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.commit,i=t.dispatch,r=e.name,a("updateTableFilterState",!1),n.next=5,st.getTableInfo(r).then((function(t){a("updateTableTitle",t.title),a("updateFieldsList",t.fields),a("resetTableMode"),t.mode&&a("updateTableMode",t.mode),a("resetGroupField"),t.group_field&&a("updateGroupField",t.group_field),a("resetFilters"),t.filters.length>0&&(a("updateFiltersModel",t.filters),i("extendFilters",t.filters)),a("resetItemsActions"),t.actions.length>0&&a("updateItemsActions",t.actions),i("getFieldsModels"),i("getFiltersItems")}));case 5:case"end":return n.stop()}}),n)})))()},getItems:function(t,e){var n=t.commit,a=e.name,i=e.params,r=void 0===i?{}:i;n("updateTableBusyState",!0),st.getData(a,r).then((function(t){n("updateTableItems",t),n("updateTableBusyState",!1)}))},getFieldsModels:function(t){var e=t.commit,n=t.getters;e("resetFieldsModels"),n.selectableFields.forEach((function(t){st.getData(t.key).then((function(n){e("updateFieldsModels",{key:[t.key],data:n})}))}))},addNewRow:function(t,e){var n=t.commit,a=t.dispatch,i=t.getters,r=t.state,s=e.table_name,o=e.row;st.addRow(s,o).then((function(t){r.table.isFiltered&&(console.log("[getItems()] filtered update"),a("getItems",{name:s,params:i.filterParams})),console.log(t),n("addTableItem",t)}))},deleteRow:function(t,e){var n=t.commit,a=e.table_name,i=e.row_id;st.deleteRow(a,i).then((function(){n("deleteTableItem",i)}))}},mutations:{updateTableBusyState:function(t,e){t.table.isBusy=e},updateTableFilterState:function(t,e){t.table.isFiltered=e},updateTableTitle:function(t,e){t.table.title=e},updateTableMode:function(t,e){t.table.mode=e},resetTableMode:function(t){t.table.mode=null},updateGroupField:function(t,e){t.table.group_field=e},resetGroupField:function(t){t.table.group_field=null},updateTableItems:function(t,e){t.table.items.list=e},updateTableItem:function(t,e){var n=e.collection,a=e.id,i=e.field,r=e.value,s=t.table.items.list.find((function(t){return t.id==a}));s[i]=r,st.updateField(n,a,{field:i,value:r})},addTableItem:function(t,e){console.log("[addTableItem()] pushing new item",e),t.table.items.list.push(e)},deleteTableItem:function(t,e){var n=t.table.items.list;n.splice(n.indexOf(n.find((function(t){return t.id==e}))),1)},resetItemsActions:function(t){t.table.items.actions=[]},updateItemsActions:function(t,e){t.table.items.actions=e},resetFieldsModels:function(t){t.table.fields.models={}},updateFieldsModels:function(t,e){var n=e.key,a=e.data;this.$app.$set(t.table.fields.models,n,a)},updateFieldsList:function(t,e){t.table.fields.list=e}},state:{table:{title:"",mode:null,group_field:null,isBusy:!1,isReadOnly:!1,isFiltered:!1,fields:{list:[],models:[]},items:{list:[],actions:[]}}},getters:{isBusy:function(t){return t.table.isBusy},isFiltered:function(t){return t.table.isFiltered},isReadOnly:function(t){return t.table.isReadOnly},title:function(t){return t.table.title},mode:function(t){return t.table.mode},groupField:function(t){return t.table.group_field},itemsData:function(t,e){return{list:t.table.items.list,actions:e.itemsActions}},fieldsData:function(t,e){return{list:e.fieldsList,models:t.table.fields.models}},fieldsList:function(t){var e=t.table.fields.list;return e.push({key:"actions",label:"Действия"}),e},itemsActions:function(t){var e=t.table.items.actions;return e.push({action:"delete"}),e},selectableFields:function(t){return t.table.fields.list.filter((function(t){return"selectable"==t.type}))},itemRowsLength:function(t){return t.table.items.list.length}}},lt=new at["a"],ct={actions:{updateSelection:function(t,e){var n=e.collection,a=e.parent,i=e.parent_id,r=e.child,s=e.child_id,o=e.value,l={parent:a,parent_id:i,child:r,value:o,mode:"many_to_many"};lt.updateField(n,s,l)},updateRadioSelection:function(t,e){var n=e.collection,a=e.parent,i=e.parent_id,r=e.child,s=e.child_id,o=e.prev,l=e.current,c={parent:a,parent_id:i,child:r,prev:o,current:l,mode:"many_to_many"};console.log(n,s,c),lt.updateField(n,s,c)}}},ut=new at["a"],dt={actions:{loadEstimateInfo:function(t){return Object(x["a"])(regeneratorRuntime.mark((function e(){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=t.state,e.next=3,ut.getEstimateInfo().then((function(t){return n.estimates=t}));case 3:case"end":return e.stop()}}),e)})))()},loadProjects:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.state,i=e.table_name,n.next=4,ut.getData(i).then((function(t){a.projects=t}));case 4:case"end":return n.stop()}}),n)})))()},loadWorks:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.state,i=e.table_name,n.next=4,ut.getData(i).then((function(t){return a.works=t}));case 4:case"end":return n.stop()}}),n)})))()},loadStages:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.state,i=e.table_name,n.next=4,ut.getData(i).then((function(t){return a.stages=t}));case 4:case"end":return n.stop()}}),n)})))()},addEstimate:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function t(){var n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.fields,t.next=3,ut.addEstimate(n).then(console.log("Success"));case 3:case"end":return t.stop()}}),t)})))()},loadTechList:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.state,i=e.table_name,n.next=4,ut.getData(i).then((function(t){return a.tech_list=t}));case 4:case"end":return n.stop()}}),n)})))()}},mutations:{updateProjectList:function(t,e){t.projects=e},resetProjectList:function(t){t.projects=[]}},state:{estimates:[],projects:[],works:[],stages:[],tech_list:[]},getters:{estimatesList:function(t){return t.estimates},projectsList:function(t){return t.projects},worksList:function(t){return t.works},baseWorksList:function(t){return t.works.filter((function(t){return 1==t.work_base}))},notBaseWorksList:function(t){return t.works.filter((function(t){return 0==t.work_base}))},stagesList:function(t){return t.stages},techList:function(t){return t.tech_list}}},ft=new at["a"],mt={actions:{fetchSidebarItems:function(t){console.log("[API info]",ft),ft.getSidebarItems().then((function(e){t.commit("updateSidebarItems",e)}))}},mutations:{updateSidebarItems:function(t,e){t.sidebar.items=e},updateObj:function(t,e){var n=e.obj,a=e.key,i=e.data;this.$app.$set(n,a,i)}},state:{sidebar:{items:[]}},getters:{sidebarItems:function(t){return t.sidebar.items}}};a["default"].use(s["a"]);var bt=new s["a"].Store({modules:{common:mt,filters:rt,table:ot,selection:ct,estimate:dt}}),pt=n("5f5b"),ht=n("b1e0");n("f9e3"),n("2dd8"),n("f843");a["default"].use(pt["a"]),a["default"].use(ht["a"]),a["default"].config.productionTip=!1;var gt=new a["default"]({router:nt,store:bt,render:function(t){return t(g)}});bt.$app=gt,gt.$mount("#app")},"688b":function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("b-row",{staticClass:"mb-4"},[n("b-col",[n("b-form-group",{staticClass:"mb-0"},[n("b-input-group",[n("b-form-input",{attrs:{id:"filter-input",type:"search",placeholder:"Введите для поиска..."},model:{value:t.filterLocal,callback:function(e){t.filterLocal=e},expression:"filterLocal"}}),n("b-input-group-append",[n("b-button",{staticClass:"rounded-0 rounded-end",attrs:{disabled:!t.filterLocal},on:{click:t.clearFilter}},[t._v(" Очистить ")])],1)],1)],1)],1)],1)},i=[],r=(n("4de4"),n("d3b7"),{props:["filter"],data:function(){return{filterLocal:this.filter}},methods:{clearFilter:function(){this.filterLocal=null,this.$emit("filterChange",this.filterLocal)}},watch:{filterLocal:function(t){this.$emit("filterChange",t)}}}),s=r,o=n("2877"),l=Object(o["a"])(s,a,i,!1,null,null,null);e["a"]=l.exports},"6c08":function(t,e,n){},"8f19":function(t,e,n){"use strict";n("1352")},d6cf:function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[""!=t.label?n("b-button",{attrs:{disabled:t.disabled,block:"",size:t.size},on:{click:function(e){return t.showFieldModal(e.target)}}},[t._v(" "+t._s(t.displayedLabel)+" ")]):n("b-skeleton",{attrs:{type:"input"}}),n("b-modal",{attrs:{id:t.fieldModal.id,title:t.fieldModal.title,"footer-bg-variant":"secondary",centered:""},on:{hide:t.resetFieldModal},scopedSlots:t._u([{key:"modal-footer",fn:function(){return[n("div",{staticClass:"d-none"})]},proxy:!0}])},[n("b-table",{attrs:{id:t.tableId,items:t.items,fields:t.fields,"per-page":t.perPage,"current-page":t.currentPage,"sort-icon-left":"",bordered:"",responsive:"",filter:t.filter},on:{filtered:t.onFiltered},scopedSlots:t._u([{key:"cell(actions)",fn:function(e){return[n("b-button",{attrs:{variant:"primary"},on:{click:function(n){return t.selectRow(e.item)}}},[t._v(" Выбрать ")])]}}])}),n("b-row",[n("b-col",[n("b-pagination",{attrs:{"total-rows":t.rows,"per-page":t.perPage,"first-number":"","last-number":"","aria-controls":t.tableId},model:{value:t.currentPage,callback:function(e){t.currentPage=e},expression:"currentPage"}})],1),n("b-col",{attrs:{cols:"4"}},[t.resetBtn?n("b-button",{staticClass:"d-block ms-auto",attrs:{variant:"danger"},on:{click:t.resetFilters}},[t._v(" Сбросить ")]):t._e()],1)],1)],1)],1)},i=[],r=0,s={props:["label","model","rowId","items","disabled","resetBtn","size"],data:function(){return r+=1,{fieldModal:{id:"field-modal-".concat(r),title:"Выберите из списка"},tableId:"table-modal-".concat(r),perPage:10,currentPage:1,filter:null,labelReplacement:""}},methods:{showFieldModal:function(t){this.$bvModal.show(this.fieldModal.id,t)},onFiltered:function(t){this.rows=t.length,this.currentPage=1},resetFilters:function(){this.$emit("resetFilters",this.rowId),this.$bvModal.hide(this.fieldModal.id)},resetFieldModal:function(){},selectRow:function(t){var e={field:this.model,value:parseInt(t.id)};this.$emit("updateField",{id:this.rowId,fields:e}),this.$emit("labelChange",{id:parseInt(t.id),model:this.model}),this.$bvModal.hide(this.fieldModal.id)}},computed:{fields:function(){return[{key:"name",sortable:!1},{key:"actions",label:" "}]},rows:function(){return this.items?this.items.length:0},displayedLabel:function(){return this.labelReplacement?this.labelReplacement:this.label}}},o=s,l=(n("fd04"),n("2877")),c=Object(l["a"])(o,a,i,!1,null,null,null);e["a"]=c.exports},f843:function(t,e,n){},fd04:function(t,e,n){"use strict";n("6c08")}});
//# sourceMappingURL=app.b3aca926.js.map