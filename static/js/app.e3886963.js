(function(t){function e(e){for(var a,i,o=e[0],l=e[1],c=e[2],u=0,d=[];u<o.length;u++)i=o[u],Object.prototype.hasOwnProperty.call(r,i)&&r[i]&&d.push(r[i][0]),r[i]=0;for(a in l)Object.prototype.hasOwnProperty.call(l,a)&&(t[a]=l[a]);f&&f(e);while(d.length)d.shift()();return s.push.apply(s,c||[]),n()}function n(){for(var t,e=0;e<s.length;e++){for(var n=s[e],a=!0,i=1;i<n.length;i++){var o=n[i];0!==r[o]&&(a=!1)}a&&(s.splice(e--,1),t=l(l.s=n[0]))}return t}var a={},i={app:0},r={app:0},s=[];function o(t){return l.p+"js/"+({dict:"dict",settings:"settings"}[t]||t)+"."+{dict:"5b664491",settings:"5b6926cc"}[t]+".js"}function l(e){if(a[e])return a[e].exports;var n=a[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,l),n.l=!0,n.exports}l.e=function(t){var e=[],n={dict:1};i[t]?e.push(i[t]):0!==i[t]&&n[t]&&e.push(i[t]=new Promise((function(e,n){for(var a="css/"+({dict:"dict",settings:"settings"}[t]||t)+"."+{dict:"044afa2a",settings:"31d6cfe0"}[t]+".css",r=l.p+a,s=document.getElementsByTagName("link"),o=0;o<s.length;o++){var c=s[o],u=c.getAttribute("data-href")||c.getAttribute("href");if("stylesheet"===c.rel&&(u===a||u===r))return e()}var d=document.getElementsByTagName("style");for(o=0;o<d.length;o++){c=d[o],u=c.getAttribute("data-href");if(u===a||u===r)return e()}var f=document.createElement("link");f.rel="stylesheet",f.type="text/css",f.onload=e,f.onerror=function(e){var a=e&&e.target&&e.target.src||r,s=new Error("Loading CSS chunk "+t+" failed.\n("+a+")");s.code="CSS_CHUNK_LOAD_FAILED",s.request=a,delete i[t],f.parentNode.removeChild(f),n(s)},f.href=r;var m=document.getElementsByTagName("head")[0];m.appendChild(f)})).then((function(){i[t]=0})));var a=r[t];if(0!==a)if(a)e.push(a[2]);else{var s=new Promise((function(e,n){a=r[t]=[e,n]}));e.push(a[2]=s);var c,u=document.createElement("script");u.charset="utf-8",u.timeout=120,l.nc&&u.setAttribute("nonce",l.nc),u.src=o(t);var d=new Error;c=function(e){u.onerror=u.onload=null,clearTimeout(f);var n=r[t];if(0!==n){if(n){var a=e&&("load"===e.type?"missing":e.type),i=e&&e.target&&e.target.src;d.message="Loading chunk "+t+" failed.\n("+a+": "+i+")",d.name="ChunkLoadError",d.type=a,d.request=i,n[1](d)}r[t]=void 0}};var f=setTimeout((function(){c({type:"timeout",target:u})}),12e4);u.onerror=u.onload=c,document.head.appendChild(u)}return Promise.all(e)},l.m=t,l.c=a,l.d=function(t,e,n){l.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},l.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},l.t=function(t,e){if(1&e&&(t=l(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(l.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)l.d(n,a,function(e){return t[e]}.bind(null,a));return n},l.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return l.d(e,"a",e),e},l.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},l.p="/",l.oe=function(t){throw console.error(t),t};var c=window["webpackJsonp"]=window["webpackJsonp"]||[],u=c.push.bind(c);c.push=e,c=c.slice();for(var d=0;d<c.length;d++)e(c[d]);var f=u;s.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"43b3":function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("nav",{staticClass:"navbar navbar-expand-lg navbar-light bg-light ps-2"},[n("div",{staticClass:"container-fluid"},[t.showBackBtn?n("div",[n("button",{staticClass:"btn btn-primary",on:{click:function(e){return t.$router.go(-1)}}},[t._v("Назад")])]):t._e(),n("span",{staticClass:"navbar-brand mb-0 me-auto",class:{"ms-4":t.showBackBtn}},[t._v(" "+t._s(t.title)+" ")])])])])},i=[],r=(n("7db0"),n("d3b7"),{props:["title","exim","back"],computed:{showBackBtn:function(){var t=this;return"true"==this.back&&!this.$store.getters.sidebarItems.find((function(e){return e.title==t.title}))}}}),s=r,o=n("2877"),l=Object(o["a"])(s,a,i,!1,null,null,null);e["a"]=l.exports},"46c2":function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("span",[n("b-button",{attrs:{variant:"danger",id:t.popId}},[t._v(" "+t._s(t.label?t.label:"Удалить")+" ")]),n("b-popover",{attrs:{target:t.popId,title:"Вы уверенны?"}},[n("b-button",{staticClass:"mr-2",attrs:{variant:"success",size:"sm"},on:{click:t.deleteRow}},[n("b-icon",{attrs:{icon:"check",variant:"light"}})],1),n("b-button",{attrs:{size:"sm"},on:{click:t.closePopover}},[t._v(" Отмена ")])],1)],1)},i=[],r=0,s={props:["label","rowId"],data:function(){return r+=1,{popId:"delete-popover-".concat(r)}},methods:{deleteRow:function(){this.closePopover(),this.$emit("deleteRow",this.rowId)},closePopover:function(){this.$root.$emit("bv::hide::popover",this.popId)}}},o=s,l=n("2877"),c=Object(l["a"])(o,a,i,!1,null,null,null);e["a"]=c.exports},"54c2":function(t,e,n){"use strict";n.d(e,"a",(function(){return u}));var a=n("1da1"),i=n("d4ec"),r=n("bee2"),s=(n("96cf"),n("99af"),n("b64b"),n("bc3a")),o=n.n(s),l=n("2b0e"),c=n("51c2");l["default"].use(c["a"]);var u=function(){function t(){Object(i["a"])(this,t),this.api="http://localhost:".concat("1337","/api"),this.version="v0.1";var e=new l["default"];this.showErrorToast=function(t){console.log(t),e.$bvToast.toast("Произошла ошибка при загрузке данных!",{title:"Ошибка",autoHideDelay:5e3,variant:"danger"})},this.showSuccessToast=function(){e.$bvToast.toast("Запрос выполнен успешно!",{title:"Успех",autoHideDelay:3e3,variant:"success"})}}return Object(r["a"])(t,[{key:"getSidebarItems",value:function(){var t=this,e=o.a.get("".concat(this.api,"/").concat(this.version,"/sidebar")),n=e.then((function(t){return t.data})).catch((function(e){return t.showErrorToast(e)}));return n}},{key:"getData",value:function(t){var e=this,n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};0!=Object.keys(n).length&&console.info("[getData() params]",n);var a=o.a.get("".concat(this.api,"/").concat(this.version,"/get/").concat(t),{params:n}),i=a.then((function(t){return t.data})).catch((function(t){return e.showErrorToast(t)}));return i}},{key:"getTableInfo",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){var n,a=this;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,o.a.get("".concat(this.api,"/").concat(this.version,"/get_dict/").concat(e)).catch((function(t){return a.showErrorToast(t)}));case 2:return n=t.sent,t.abrupt("return",n.data);case 4:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"getTablesInfo",value:function(){var t=this,e=o.a.get("".concat(this.api,"/").concat(this.version,"/get_dict")),n=e.then((function(t){return t.data})).catch((function(e){return t.showErrorToast(e)}));return n}},{key:"updateField",value:function(t,e,n){var a=this,i=o.a.put("".concat(this.api,"/").concat(this.version,"/update/").concat(t,"/").concat(e),n),r=i.then((function(t){return t.data})).catch((function(t){return a.showErrorToast(t)}));return r}},{key:"addRow",value:function(t,e){var n=this;console.log("[addRow() params]",t,e);var a=o.a.post("".concat(this.api,"/").concat(this.version,"/add/").concat(t),e),i=a.then((function(t){return t.data})).catch((function(t){return n.showErrorToast(t)}));return i}},{key:"deleteRow",value:function(t,e){var n=this,a=o.a.delete("".concat(this.api,"/").concat(this.version,"/delete/").concat(t,"/").concat(e)),i=a.then((function(t){return t.data})).catch((function(t){return n.showErrorToast(t)}));return i}},{key:"getEstimateInfo",value:function(){var t=this,e=o.a.get("".concat(this.api,"/").concat(this.version,"/get_estimate_records")),n=e.then((function(t){return t.data})).catch((function(e){return t.showErrorToast(e)}));return n}},{key:"addEstimate",value:function(t){var e=this,n=o.a.post("".concat(this.api,"/").concat(this.version,"/calculate_estimate"),t),a=n.then((function(t){return t.data})).catch((function(t){return e.showErrorToast(t)}));return a}},{key:"deleteEstimate",value:function(t){var e=this,n=o.a.delete("".concat(this.api,"/").concat(this.version,"/delete_estimate/").concat(t)),a=n.then((function(t){return t.data})).catch((function(t){return e.showErrorToast(t)}));return a}},{key:"getEstimateMaterials",value:function(t){var e=this,n=o.a.get("".concat(this.api,"/").concat(this.version,"/get_estimate_materials/").concat(t)),a=n.then((function(t){return t.data})).catch((function(t){return e.showErrorToast(t)}));return a}},{key:"getEstimateWorks",value:function(t){var e=this,n=o.a.get("".concat(this.api,"/").concat(this.version,"/get_estimate_works/").concat(t)),a=n.then((function(t){return t.data})).catch((function(t){return e.showErrorToast(t)}));return a}},{key:"importTable",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){var n=this;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,o.a.post("".concat(this.api,"/").concat(this.version,"/import/").concat(e)).then((function(){return n.showSuccessToast()})).catch((function(t){return n.showErrorToast(t)}));case 2:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()},{key:"exportTable",value:function(){var t=Object(a["a"])(regeneratorRuntime.mark((function t(e){var n=this;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,o.a.get("".concat(this.api,"/").concat(this.version,"/export/").concat(e)).then((function(){return n.showSuccessToast()})).catch((function(t){return n.showErrorToast(t)}));case 2:case"end":return t.stop()}}),t,this)})));function e(e){return t.apply(this,arguments)}return e}()}]),t}()},"56d7":function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var a=n("2b0e"),i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{ref:"root",staticClass:"d-flex",attrs:{id:"app"}},[n("side-bar",{attrs:{items:t.sidebarItems}}),n("div",{staticClass:"d-flex flex-column w-100 overflow-hidden"},[n("router-view")],1)],1)},r=[],s=n("2f62"),o=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"d-flex flex-column flex-shrink-0 p-3 bg-light vh-100 shadow",staticStyle:{width:"280px","z-index":"1"}},[n("a",{staticClass:"d-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none",attrs:{href:"/"}},[n("b-iconstack",{staticClass:"me-3",attrs:{"font-scale":"2"}},[n("b-icon",{attrs:{stacked:"",icon:"gear-wide",scale:"1.5"}}),n("b-icon",{attrs:{stacked:"",icon:"wrench",scale:"0.75","flip-h":""}}),n("b-icon",{attrs:{stacked:"",icon:"hammer",scale:"0.75"}})],1),n("span",{staticClass:"fs-4"},[t._v("Automation Build")])],1),n("hr"),n("ul",{staticClass:"nav nav-pills flex-column"},[n("li",{staticClass:"nav-item"},[n("router-link",{staticClass:"nav-link link-dark",attrs:{to:"/","exact-active-class":"active"}},[n("b-icon",{staticClass:"me-1",attrs:{icon:"calculator",variant:"dark"}}),t._v(" Расчеты ")],1)],1)]),n("hr"),n("ul",{staticClass:"nav nav-pills flex-column mb-auto"},t._l(t.items,(function(e){return n("li",{key:e.id},[n("router-link",{staticClass:"nav-link link-dark",attrs:{to:{name:"dict",params:{name:e.name}},"active-class":"active"}},[n("b-icon",{staticClass:"me-1",attrs:{icon:e.icon,variant:"dark"}}),t._v(" "+t._s(e.title)+" ")],1)],1)})),0),n("hr"),n("ul",{staticClass:"nav nav-pills flex-column"},[n("li",[n("router-link",{staticClass:"nav-link link-dark",attrs:{to:"/settings","exact-active-class":"active"}},[n("b-icon",{staticClass:"me-1",attrs:{icon:"gear",variant:"dark"}}),t._v(" Настройки ")],1)],1)])])},l=[],c={props:["items"]},u=c,d=(n("f6e9"),n("2877")),f=Object(d["a"])(u,o,l,!1,null,"761e6ce8",null),m=f.exports,h={components:{SideBar:m},computed:Object(s["c"])(["sidebarItems"]),methods:Object(s["b"])(["fetchSidebarItems"]),mounted:function(){this.fetchSidebarItems()}},p=h,b=Object(d["a"])(p,i,r,!1,null,null,null),g=b.exports,v=(n("d3b7"),n("3ca3"),n("ddb0"),n("8c4f")),k=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("Title",{attrs:{title:t.title,back:"false"}}),n("b-container",{staticClass:"p-4",attrs:{fluid:""}},[n("b-row",[n("b-col",{attrs:{cols:"12",xl:"8"}},[t.isEditing?t._e():n("EstimatesTable",{on:{toggleEditingView:t.onToggleView}}),t.isEditing?n("EstimateForm",{attrs:{id:t.editingId},on:{toggleEditingView:t.onToggleView}}):t._e(),t.isEditing?t._e():n("b-button",{attrs:{variant:"primary"},on:{click:function(e){return t.onToggleView(!0,-1)}}},[t._v(" Добавить ")])],1)],1)],1)],1)},w=[],_=n("43b3"),y=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("search-bar",{attrs:{filter:t.searchFilter},on:{filterChange:t.onFilterChange}}),n("b-table",{staticClass:"text-nowrap",attrs:{fields:t.fields,items:t.estimatesList,filter:t.searchFilter,id:"table","head-variant":"light",bordered:"",responsive:"","show-empty":""},scopedSlots:t._u([{key:"cell(actions)",fn:function(e){return[n("b-button",{staticClass:"mr-2",attrs:{variant:"success"},on:{click:function(n){return t.exportToExcel(e.item.id)}}},[t._v(" Выгрузить в Excel ")]),n("b-button",{staticClass:"mr-2",on:{click:e.toggleDetails}},[t._v(" Подробнее "+t._s(e.detailsShowing?"↑":"↓")+" ")]),n("delete-row-btn",{attrs:{rowId:e.item.id},on:{deleteRow:t.onDeleteRow}})]}},{key:"table-busy",fn:function(){return[n("div",{staticClass:"text-center my-2"},[n("b-spinner",{staticClass:"align-middle me-2"}),n("strong",[t._v("Загрузка...")])],1)]},proxy:!0},{key:"row-details",fn:function(e){return[n("b-row",{staticClass:"mb-2"},[n("b-col",[n("b",[t._v("Цена заказчика:")]),t._v(" "+t._s(e.item.price_client))]),n("b-col",{staticClass:"text-right"},[n("EstimateModal",{staticClass:"mr-2",attrs:{label:"Материалы",childId:e.item.id,type:"materials"}}),n("EstimateModal",{staticClass:"mr-2",attrs:{label:"Работы",childId:e.item.id,type:"works"}})],1)],1)]}}])})],1)},j=[],x=n("1da1"),E=n("5530"),O=(n("96cf"),n("688b")),F=n("46c2"),T=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("span",[n("b-button",{on:{click:function(e){return t.showFieldModal(e.target)}}},[t._v(" "+t._s(t.label)+" ")]),n("b-modal",{attrs:{id:t.modalId,title:t.label,size:"lg","footer-bg-variant":"secondary",centered:""},scopedSlots:t._u([{key:"modal-footer",fn:function(){return[n("div",{staticClass:"d-none"})]},proxy:!0}])},[n("SearchBar",{attrs:{filter:t.searchFilter},on:{filterChange:t.onFilterChange}}),n("b-table",{attrs:{id:t.tableId,items:t.estimateModalList,fields:t.fields,"per-page":t.perPage,"current-page":t.currentPage,filter:t.searchFilter,bordered:"","show-empty":"",responsive:""}}),n("b-row",[n("b-col",[n("b-pagination",{attrs:{"total-rows":t.rows,"per-page":t.perPage,"first-number":"","last-number":"","aria-controls":t.tableId},model:{value:t.currentPage,callback:function(e){t.currentPage=e},expression:"currentPage"}})],1)],1)],1)],1)},I=[],C=(n("99af"),{components:{SearchBar:O["a"]},props:["label","childId","type"],data:function(){return{modalId:"estimate-".concat(this.childId,"-modal-").concat(this.type),tableId:"estimate-".concat(this.childId,"-modal-").concat(this.type,"-table"),searchFilter:null,perPage:8,currentPage:1,fields:[{key:"name",label:"Наименование"}]}},computed:Object(E["a"])(Object(E["a"])({},Object(s["c"])(["estimateModalList"])),{},{rows:function(){return this.items?this.items.length:0}}),methods:Object(E["a"])(Object(E["a"])({},Object(s["b"])(["loadEstimateMaterials","loadEstimateWorks"])),{},{showFieldModal:function(t){this.$bvModal.show(this.modalId,t),"materials"==this.type?(this.loadEstimateMaterials({id:this.childId}),this.fields=[{key:"material_name",label:"Наименование"},{key:"amount",label:"Кол-во"},{key:"price",label:"Цена"}]):(this.loadEstimateWorks({id:this.childId}),this.fields=[{key:"work_name",label:"Наименование"},{key:"client_price",label:"Цена клиента"},{key:"base_price",label:"Цена себестоимости"}])},onFilterChange:function(t){this.searchFilter=t}}),mounted:function(){}}),L=C,R=(n("a814"),Object(d["a"])(L,T,I,!1,null,null,null)),M=R.exports,S={components:{SearchBar:O["a"],DeleteRowBtn:F["a"],EstimateModal:M},data:function(){return{searchFilter:null,fields:[{key:"client_fio",label:"Наименование"},{key:"actions",label:"Действия"}]}},computed:Object(E["a"])({},Object(s["c"])(["estimatesList"])),methods:Object(E["a"])(Object(E["a"])({},Object(s["b"])(["loadEstimateInfo","deleteEstimate"])),{},{init:function(){var t=this;return Object(x["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:t.loadEstimateInfo();case 1:case"end":return e.stop()}}),e)})))()},onFilterChange:function(t){this.searchFilter=t},onDeleteRow:function(t){this.deleteEstimate({table_name:"estimate",id:t})},exportToExcel:function(t){console.log("TODO: implement exportToExcel(".concat(t,")"))},editEstimate:function(t){this.$emit("toggleEditingView",!0,t)}}),mounted:function(){this.init()}},B=S,P=Object(d["a"])(B,y,j,!1,null,null,null),$=P.exports,W=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("b-row",{staticClass:"my-2"},[n("b-col",{attrs:{sm:"3"}},[n("label",{attrs:{for:"name-input"}},[t._v("ФИО:")])]),n("b-col",{attrs:{sm:"9"}},[n("b-form-input",{attrs:{id:"name-input",placeholder:"Введите ваше ФИО"},model:{value:t.name,callback:function(e){t.name=e},expression:"name"}})],1)],1),n("b-row",{staticClass:"my-2"},[n("b-col",{attrs:{sm:"3"}},[n("label",{attrs:{for:"name-input"}},[t._v("Проект:")])]),n("b-col",{attrs:{sm:"9"}},[n("change-field-modal",{ref:"project-input",attrs:{label:"Не выбрано",model:"project-input",rowId:"-1",items:t.projectsList},on:{updateField:t.onProjectInputUpdate,labelChange:t.onProjectLabelChange}})],1)],1),n("b-row",{staticClass:"my-2"},[n("b-col",{attrs:{sm:"3"}},[n("label",{attrs:{for:"name-input"}},[t._v("Базовая комплектация:")])]),n("b-col",{attrs:{sm:"9"}},[n("b-form-checkbox",{attrs:{size:"lg"},model:{value:t.isBaseEquipment,callback:function(e){t.isBaseEquipment=e},expression:"isBaseEquipment"}})],1)],1),n("BaseTable",{staticClass:"mb-4",attrs:{showBase:t.isBaseEquipment},on:{updateAdditionalWorks:t.onUpdateAdditionalWorks}}),t.isBaseEquipment?t._e():n("StagesTable",{staticClass:"mb-4",on:{updateWorkTechnologies:t.onUpdateWorkTechnologies}}),n("b-row",{staticClass:"my-2"},[n("b-col",{attrs:{cols:"2"}},[n("b-button",{attrs:{variant:"primary"},on:{click:t.saveEstimate}},[t._v(" Сохранить ")])],1),n("b-col",{staticClass:"text-end"},[n("b-button",{attrs:{variant:"danger"},on:{click:function(e){return t.$emit("toggleEditingView",!1)}}},[t._v(" Отмена ")])],1)],1)],1)},A=[],D=(n("7db0"),n("b0c0"),n("d6cf")),q=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[t.showBase?n("b-card",{staticClass:"mb-4",attrs:{"no-body":0!=t.baseWorksList.length,header:"Базовые работы"}},[0==t.baseWorksList.length?n("div",[t._v(" Базовые работы отсутствуют! ")]):n("b-list-group",{attrs:{flush:""}},t._l(t.baseWorksList,(function(e){return n("b-list-group-item",{key:e.id},[t._v(t._s(e.name))])})),1)],1):t._e(),n("b-card",{staticClass:"mb-2",attrs:{"no-body":0!=t.notBaseWorksList.length,header:"Дополнительные работы"}},[0==t.notBaseWorksList.length?n("div",[t._v(" Дополнительные работы отсутствуют! ")]):n("b-list-group",{attrs:{flush:""}},t._l(t.notBaseWorksList,(function(e){return n("b-list-group-item",{key:e.id},[n("b-form-checkbox",{attrs:{value:e.id},model:{value:t.selectedAdditionalWorks,callback:function(e){t.selectedAdditionalWorks=e},expression:"selectedAdditionalWorks"}},[t._v(t._s(e.name))])],1)})),1)],1)],1)},z=[],U={props:["showBase"],data:function(){return{selectedAdditionalWorks:[]}},computed:Object(E["a"])({},Object(s["c"])(["worksList","baseWorksList","notBaseWorksList"])),methods:Object(E["a"])(Object(E["a"])({},Object(s["b"])(["loadWorks"])),{},{init:function(){var t=this;return Object(x["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:t.loadWorks({table_name:"work"});case 1:case"end":return e.stop()}}),e)})))()}}),watch:{selectedAdditionalWorks:function(t){this.$emit("updateAdditionalWorks",t)}},mounted:function(){this.init()}},V=U,N=Object(d["a"])(V,q,z,!1,null,null,null),G=N.exports,H=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("b-card",{staticClass:"mb-2",attrs:{"no-body":"",header:"Стадии работ"}},[n("b-list-group",{attrs:{flush:""}},t._l(t.stagesList,(function(e){return n("b-list-group-item",{key:e.id},[n("b-row",[n("b-col",[n("b-form-checkbox",{attrs:{value:e.id},model:{value:t.selectedStages,callback:function(e){t.selectedStages=e},expression:"selectedStages"}},[t._v(t._s(e.name))])],1),n("b-col",{staticClass:"text-end"},[t.selectedStages.includes(e.id)?n("change-field-modal",{ref:"tech-field-"+e.id,refInFor:!0,staticClass:"negative-margin",attrs:{label:"Выберите технологию",model:t.techModel,rowId:e.id,items:t.techList.filter((function(t){return t.work_stage==e.id})),size:"sm"},on:{updateField:t.onUpdateField}}):t._e()],1)],1)],1)})),1)],1)],1)},J=[],K=(n("4de4"),n("caad"),n("2532"),n("a434"),{components:{ChangeFieldModal:D["a"]},data:function(){return{fields:[{key:"checked",label:" "},{key:"name",label:"Наименование"},{key:"actions",label:" "}],stageModel:"work_stage",selectedStages:[],techModel:"work_technology",selectedWorkTech:[]}},computed:Object(E["a"])({},Object(s["c"])(["stagesList","techList"])),methods:Object(E["a"])(Object(E["a"])({},Object(s["b"])(["loadStages","loadTechList"])),{},{onUpdateField:function(t){var e=t.id,n=t.fields;this.$set(this.selectedWorkTech,e,n.value),this.$refs["tech-field-".concat(e)][0].labelReplacement=this.getFieldById(n.value,this.techModel,"name")},getFieldById:function(t,e,n){return this.techList.find((function(e){return e.id==t}))[n]}}),watch:{selectedWorkTech:function(t){this.$emit("updateWorkTechnologies",t.filter(Boolean))},selectedStages:function(t,e){var n=e.filter((function(e){return!t.includes(e)}));n[0]&&this.selectedWorkTech.splice(n,1)}},mounted:function(){this.loadStages({table_name:this.stageModel}),this.loadTechList({table_name:this.techModel})}}),Q=K,X=(n("b765"),Object(d["a"])(Q,H,J,!1,null,"14da652c",null)),Y=X.exports,Z={components:{ChangeFieldModal:D["a"],BaseTable:G,StagesTable:Y},props:["id"],data:function(){return{name:null,selectedProjectId:null,selectedAdditionalWorks:[],selectedWorkTechnologies:[],isBaseEquipment:!0,isEditing:!1}},computed:Object(E["a"])({},Object(s["c"])(["projectsList"])),methods:Object(E["a"])(Object(E["a"])({},Object(s["b"])(["loadProjects","addEstimate"])),{},{init:function(){var t=this;return Object(x["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:t.loadProjects({table_name:"project"}),null!=t.id&&-1!=t.id&&console.log("editing estiamte with id "+t.id);case 2:case"end":return e.stop()}}),e)})))()},getFieldById:function(t,e,n){return this.projectsList.find((function(e){return e.id==t}))[n]},onProjectLabelChange:function(t){var e=t.id,n=t.model;this.$refs["project-input"].labelReplacement=this.getFieldById(e,n,"name")},onProjectInputUpdate:function(t){t._id;var e=t.fields;this.selectedProjectId=e.value},onUpdateAdditionalWorks:function(t){this.selectedAdditionalWorks=t},onUpdateWorkTechnologies:function(t){this.selectedWorkTechnologies=t},saveEstimate:function(){var t=this;return Object(x["a"])(regeneratorRuntime.mark((function e(){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=Object(E["a"])(Object(E["a"])({client_info:t.name,use_base:t.isBaseEquipment,project_id:t.selectedProjectId},t.selectedAdditionalWorks.length&&{additional_works:t.selectedAdditionalWorks}),t.selectedWorkTechnologies.length&&{work_technologies:t.selectedWorkTechnologies}),console.table(n),e.next=4,t.addEstimate({fields:n}).then((function(e){console.log(e),t.$emit("toggleEditingView",!1)}));case 4:case"end":return e.stop()}}),e)})))()}}),mounted:function(){this.init()}},tt=Z,et=Object(d["a"])(tt,W,A,!1,null,null,null),nt=et.exports,at={components:{Title:_["a"],EstimateForm:nt,EstimatesTable:$},data:function(){return{title:"Расчеты",isEditing:!1,editingId:null}},methods:{onToggleView:function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:-1;this.isEditing=t,this.editingId=e}}},it=at,rt=Object(d["a"])(it,k,w,!1,null,null,null),st=rt.exports;a["default"].use(v["a"]);var ot=[{path:"/",name:"Расчеты",component:st},{path:"/dict/:name",name:"dict",props:!0,component:function(){return n.e("dict").then(n.bind(null,"29a8"))}},{path:"/dict/:parent/:name/:id",name:"child-dict",props:!0,component:function(){return n.e("dict").then(n.bind(null,"29a8"))}},{path:"/settings",name:"settings",component:function(){return n.e("settings").then(n.bind(null,"26d3"))}}],lt=new v["a"]({mode:"history",base:"/",routes:ot}),ct=lt,ut=(n("159b"),n("c740"),n("54c2")),dt=new ut["a"],ft={actions:{getFiltersItems:function(t){var e=t.commit,n=t.state;e("resetFilterList"),n.filters.model.forEach((function(t){dt.getData(t.key).then((function(n){e("updateFilterList",{key:[t.key],data:n})}))}))},extendFilters:function(t,e){var n=t.commit,a=t.state;e.forEach((function(t,e){n("updateObj",{obj:a.filters.model[e],key:"disabled",data:0!=e}),n("updateObj",{obj:a.filters.model[e],key:"text",data:"Не выбрано"}),n("updateObj",{obj:a.filters.state,key:[t.key],data:""})}))},resetFiltersFromId:function(t){for(var e=t.commit,n=t.state,a=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0,i=a;i<n.filters.model.length;i++)e("resetFilterLabel",{model:n.filters.model[i].key}),e("updateObj",{obj:n.filters.model[i],key:"disabled",data:i!=a}),e("updateObj",{obj:n.filters.state,key:n.filters.model[i].key,data:""});0==a&&e("updateTableFilterState",!1)},applyFilters:function(t,e){var n=t.commit,a=t.state,i=a.filters.model.findIndex((function(t){return t.key==e.field}));i!=a.filters.model.length-1&&n("updateObj",{obj:a.filters.model[i+1],key:"disabled",data:!1}),n("updateTableFilterState",!0),n("updateObj",{obj:a.filters.state,key:e.field,data:e.value})}},mutations:{resetFilterList:function(t){t.filters.list={}},resetFilters:function(t){t.filters.list={},t.filters.model=[],t.filters.state={}},resetFilterLabel:function(t,e){var n=e.model;t.filters.model.find((function(t){return t.key==n})).text="Не выбрано"},updateFiltersModel:function(t,e){t.filters.model=e},updateFilterList:function(t,e){var n=e.key,a=e.data;this.$app.$set(t.filters.list,n,a)},updateFilterLabel:function(t,e){var n=e.itemId,a=e.model;t.filters.model.find((function(t){return t.key==a})).text=t.filters.list[a].find((function(t){return t.id==n}))["name"]}},state:{filters:{model:[],list:{},state:{}}},getters:{filtersData:function(t){return t.filters},filterParams:function(t){return Object(E["a"])(Object(E["a"])({},t.filters.state),{mode:"advanced_filters"})}}},mt=new ut["a"],ht={actions:{getTableInfo:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i,r;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.commit,i=t.dispatch,r=e.name,a("updateTableBusyState",!0),a("updateTableFilterState",!1),n.next=6,mt.getTableInfo(r).then((function(t){a("updateTableTitle",t.title),a("updateFieldsList",t.fields),a("resetTableMode"),t.mode&&a("updateTableMode",t.mode),a("resetGroupField"),t.group_field&&a("updateGroupField",t.group_field),a("resetFilters"),t.filters.length>0&&(a("updateFiltersModel",t.filters),i("extendFilters",t.filters)),a("resetItemsActions"),t.actions.length>0&&a("updateItemsActions",t.actions),i("getFieldsModels"),i("getFiltersItems")}));case 6:case"end":return n.stop()}}),n)})))()},getItems:function(t,e){var n=t.commit,a=e.name,i=e.params,r=void 0===i?{}:i;console.log("[getItems() params:",r),mt.getData(a,r).then((function(t){n("updateTableItems",t),n("updateTableBusyState",!1)}))},getFieldsModels:function(t){var e=t.commit,n=t.getters;e("resetFieldsModels"),n.selectableFields.forEach((function(t){mt.getData(t.key).then((function(n){e("updateFieldsModels",{key:[t.key],data:n})}))}))},addNewRow:function(t,e){var n=t.commit,a=t.dispatch,i=t.getters,r=t.state,s=e.table_name,o=e.row;mt.addRow(s,o).then((function(t){r.table.isFiltered&&(console.log("[getItems()] filtered update"),a("getItems",{name:s,params:i.filterParams})),n("addTableItem",t)}))},deleteRow:function(t,e){var n=t.commit,a=e.table_name,i=e.row_id;mt.deleteRow(a,i).then((function(){n("deleteTableItem",i)}))}},mutations:{updateTableBusyState:function(t,e){t.table.isBusy=e},updateTableFilterState:function(t,e){t.table.isFiltered=e},updateTableTitle:function(t,e){t.table.title=e},updateTableMode:function(t,e){t.table.mode=e},resetTableMode:function(t){t.table.mode=null},updateGroupField:function(t,e){t.table.group_field=e},resetGroupField:function(t){t.table.group_field=null},updateTableItems:function(t,e){t.table.items.list=e},updateTableItem:function(t,e){var n=e.collection,a=e.id,i=e.field,r=e.value,s=t.table.items.list.find((function(t){return t.id==a}));s[i]=r,mt.updateField(n,a,{field:i,value:r})},addTableItem:function(t,e){console.log("[addTableItem()] pushing new item",e),t.table.items.list.push(e)},deleteTableItem:function(t,e){var n=t.table.items.list;n.splice(n.indexOf(n.find((function(t){return t.id==e}))),1)},resetItemsActions:function(t){t.table.items.actions=[]},updateItemsActions:function(t,e){t.table.items.actions=e},resetFieldsModels:function(t){t.table.fields.models={}},updateFieldsModels:function(t,e){var n=e.key,a=e.data;this.$app.$set(t.table.fields.models,n,a)},updateFieldsList:function(t,e){t.table.fields.list=e}},state:{table:{title:"",mode:null,group_field:null,isBusy:!1,isReadOnly:!1,isFiltered:!1,fields:{list:[],models:[]},items:{list:[],actions:[]}}},getters:{isBusy:function(t){return t.table.isBusy},isFiltered:function(t){return t.table.isFiltered},isReadOnly:function(t){return t.table.isReadOnly},title:function(t){return t.table.title},mode:function(t){return t.table.mode},groupField:function(t){return t.table.group_field},itemsData:function(t,e){return{list:t.table.items.list,actions:e.itemsActions}},fieldsData:function(t,e){return{list:e.fieldsList,models:t.table.fields.models}},fieldsList:function(t){var e=t.table.fields.list;return e.push({key:"actions",label:"Действия"}),e},itemsActions:function(t){var e=t.table.items.actions;return e.push({action:"delete"}),e},selectableFields:function(t){return t.table.fields.list.filter((function(t){return"selectable"==t.type}))},itemRowsLength:function(t){return t.table.items.list.length}}},pt=new ut["a"],bt={actions:{updateSelection:function(t,e){var n=e.collection,a=e.parent,i=e.parent_id,r=e.child,s=e.child_id,o=e.value,l={parent:a,parent_id:i,child:r,value:o,mode:"many_to_many"};pt.updateField(n,s,l)},updateRadioSelection:function(t,e){var n=e.collection,a=e.parent,i=e.parent_id,r=e.child,s=e.child_id,o=e.prev,l=e.current,c={parent:a,parent_id:i,child:r,prev:o,current:l,mode:"many_to_many"};pt.updateField(n,s,c)}}},gt=new ut["a"],vt={actions:{loadEstimateInfo:function(t){return Object(x["a"])(regeneratorRuntime.mark((function e(){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=t.state,e.next=3,gt.getEstimateInfo().then((function(t){return n.estimates=t}));case 3:case"end":return e.stop()}}),e)})))()},loadProjects:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.state,i=e.table_name,n.next=4,gt.getData(i).then((function(t){a.projects=t}));case 4:case"end":return n.stop()}}),n)})))()},loadWorks:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.state,i=e.table_name,n.next=4,gt.getData(i).then((function(t){return a.works=t}));case 4:case"end":return n.stop()}}),n)})))()},loadStages:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.state,i=e.table_name,n.next=4,gt.getData(i).then((function(t){return a.stages=t}));case 4:case"end":return n.stop()}}),n)})))()},addEstimate:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function t(){var n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.fields,t.next=3,gt.addEstimate(n).then((function(t){return t}));case 3:return t.abrupt("return",t.sent);case 4:case"end":return t.stop()}}),t)})))()},deleteEstimate:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.state,i=e.id,n.next=4,gt.deleteEstimate(i).then((function(t){a.estimates.splice(a.estimates.indexOf(a.estimates.find((function(t){return t.id==i}))),1)}));case 4:case"end":return n.stop()}}),n)})))()},loadTechList:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.state,i=e.table_name,n.next=4,gt.getData(i).then((function(t){return a.tech_list=t}));case 4:case"end":return n.stop()}}),n)})))()},loadEstimateMaterials:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.state,i=e.id,n.next=4,gt.getEstimateMaterials(i).then((function(t){return a.estimate_modal_list=t}));case 4:case"end":return n.stop()}}),n)})))()},loadEstimateWorks:function(t,e){return Object(x["a"])(regeneratorRuntime.mark((function n(){var a,i;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return a=t.state,i=e.id,n.next=4,gt.getEstimateWorks(i).then((function(t){return a.estimate_modal_list=t}));case 4:case"end":return n.stop()}}),n)})))()}},mutations:{updateProjectList:function(t,e){t.projects=e},resetProjectList:function(t){t.projects=[]},resetEstimateModalList:function(t){t.estimate_modal_list=[]}},state:{estimates:[],projects:[],works:[],stages:[],tech_list:[],estimate_modal_list:[]},getters:{estimatesList:function(t){return t.estimates},projectsList:function(t){return t.projects},worksList:function(t){return t.works},baseWorksList:function(t){return t.works.filter((function(t){return 1==t.work_base}))},notBaseWorksList:function(t){return t.works.filter((function(t){return 0==t.work_base}))},stagesList:function(t){return t.stages},techList:function(t){return t.tech_list},estimateModalList:function(t){return t.estimate_modal_list}}},kt=new ut["a"],wt={actions:{fetchSidebarItems:function(t){console.log("[API info]",kt),kt.getSidebarItems().then((function(e){t.commit("updateSidebarItems",e)}))}},mutations:{updateSidebarItems:function(t,e){t.sidebar.items=e},updateObj:function(t,e){var n=e.obj,a=e.key,i=e.data;this.$app.$set(n,a,i)}},state:{sidebar:{items:[]}},getters:{sidebarItems:function(t){return t.sidebar.items}}};a["default"].use(s["a"]);var _t=new s["a"].Store({modules:{common:wt,filters:ft,table:ht,selection:bt,estimate:vt}}),yt=n("5f5b"),jt=n("b1e0");n("f9e3"),n("2dd8"),n("f843");a["default"].use(yt["a"]),a["default"].use(jt["a"]),a["default"].config.productionTip=!1;var xt=new a["default"]({router:ct,store:_t,render:function(t){return t(g)}});_t.$app=xt,xt.$mount("#app")},"688b":function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("b-row",{staticClass:"mb-4"},[n("b-col",[n("b-form-group",{staticClass:"mb-0"},[n("b-input-group",[n("b-form-input",{attrs:{id:"filter-input",type:"search",placeholder:"Введите для поиска..."},model:{value:t.filterLocal,callback:function(e){t.filterLocal=e},expression:"filterLocal"}}),n("b-input-group-append",[n("b-button",{attrs:{disabled:!t.filterLocal},on:{click:t.clearFilter}},[t._v(" Очистить ")])],1)],1)],1)],1)],1)},i=[],r=(n("4de4"),n("d3b7"),{props:["filter"],data:function(){return{filterLocal:this.filter}},methods:{clearFilter:function(){this.filterLocal=null,this.$emit("filterChange",this.filterLocal)}},watch:{filterLocal:function(t){this.$emit("filterChange",t)}}}),s=r,o=n("2877"),l=Object(o["a"])(s,a,i,!1,null,null,null);e["a"]=l.exports},"6c08":function(t,e,n){},"6d9a":function(t,e,n){},"742c":function(t,e,n){},a814:function(t,e,n){"use strict";n("e1ac")},b765:function(t,e,n){"use strict";n("6d9a")},d6cf:function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[""!=t.label?n("b-button",{attrs:{disabled:t.disabled,block:"",size:t.size},on:{click:function(e){return t.showFieldModal(e.target)}}},[t._v(" "+t._s(t.displayedLabel)+" ")]):n("b-skeleton",{attrs:{type:"input"}}),n("b-modal",{attrs:{id:t.fieldModal.id,title:t.fieldModal.title,"footer-bg-variant":"secondary",centered:""},on:{hide:t.resetFieldModal},scopedSlots:t._u([{key:"modal-footer",fn:function(){return[n("div",{staticClass:"d-none"})]},proxy:!0}])},[n("SearchBar",{attrs:{filter:t.searchFilter},on:{filterChange:t.onFilterChange}}),n("b-table",{attrs:{id:t.tableId,items:t.items,fields:t.fields,"per-page":t.perPage,"current-page":t.currentPage,filter:t.searchFilter,bordered:"","show-empty":"",responsive:""},scopedSlots:t._u([{key:"cell(actions)",fn:function(e){return[n("b-button",{attrs:{variant:"primary"},on:{click:function(n){return t.selectRow(e.item)}}},[t._v(" Выбрать ")])]}}])}),n("b-row",[n("b-col",[n("b-pagination",{attrs:{"total-rows":t.rows,"per-page":t.perPage,"first-number":"","last-number":"","aria-controls":t.tableId},model:{value:t.currentPage,callback:function(e){t.currentPage=e},expression:"currentPage"}})],1),n("b-col",{attrs:{cols:"4"}},[t.resetBtn?n("b-button",{staticClass:"d-block ms-auto",attrs:{variant:"danger"},on:{click:t.resetFilters}},[t._v(" Сбросить ")]):t._e()],1)],1)],1)],1)},i=[],r=n("688b"),s=0,o={components:{SearchBar:r["a"]},props:["label","model","rowId","items","disabled","resetBtn","size"],data:function(){return s+=1,{fieldModal:{id:"field-modal-".concat(s),title:"Выберите из списка"},tableId:"table-modal-".concat(s),perPage:8,currentPage:1,filter:null,labelReplacement:"",searchFilter:null}},methods:{showFieldModal:function(t){this.$bvModal.show(this.fieldModal.id,t)},onFilterChange:function(t){this.searchFilter=t},resetFilters:function(){this.$emit("resetFilters",this.rowId),this.$bvModal.hide(this.fieldModal.id)},resetFieldModal:function(){},selectRow:function(t){var e={field:this.model,value:parseInt(t.id)};this.$emit("updateField",{id:this.rowId,fields:e}),this.$emit("labelChange",{id:parseInt(t.id),model:this.model}),this.$bvModal.hide(this.fieldModal.id)}},computed:{fields:function(){return[{key:"name",sortable:!1},{key:"actions",label:" "}]},rows:function(){return this.items?this.items.length:0},displayedLabel:function(){return this.labelReplacement?this.labelReplacement:this.label}}},l=o,c=(n("fd04"),n("2877")),u=Object(c["a"])(l,a,i,!1,null,null,null);e["a"]=u.exports},e1ac:function(t,e,n){},f6e9:function(t,e,n){"use strict";n("742c")},f843:function(t,e,n){},fd04:function(t,e,n){"use strict";n("6c08")}});
//# sourceMappingURL=app.e3886963.js.map