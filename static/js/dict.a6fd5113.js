(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["dict"],{"29a8":function(e,t,a){"use strict";a.r(t);var i=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("Title",{attrs:{title:e.title,back:"true"}}),a("b-container",{staticClass:"p-4",attrs:{fluid:""}},[a("b-row",[a("b-col",{attrs:{cols:"12"}},[null==e.mode?a("search-bar",{attrs:{filter:e.searchFilter},on:{filterChange:e.onFilterChange}}):e._e(),0!=e.filtersData.model.length?a("Filters",{ref:"filters",attrs:{filtersData:e.filtersData},on:{applyFilters:e.onApplyFilters,resetFilters:e.onResetFilters,filterLabelChange:e.onFilterLabelChange}}):e._e(),null==e.mode?a("Table",{attrs:{parent:e.parent,itemsData:e.itemsData,fieldsData:e.fieldsData,filter:e.searchFilter,isBusy:e.isBusy,perPage:e.perPage,currentPage:e.currentPage,name:e.name}}):e._e(),a("b-row",[a("b-col",{attrs:{cols:"12",lg:"10",xl:"8"}},[null!=e.mode&&null==e.groupField?a("SelectGroup",{attrs:{items:e.itemsData,fields:e.fieldsData,id:e.id,name:e.name}}):e._e(),null!=e.mode&&null!=e.groupField?a("RadioGroup",{attrs:{items:e.itemsData,groupField:e.groupField,fields:e.fieldsData,id:e.id,name:e.name}}):e._e()],1)],1),null==e.mode?a("b-row",[a("b-col",{attrs:{cols:"10"}},[a("Pagination",{attrs:{rows:e.itemRowsLength,perPage:e.perPage,currentPage:e.currentPage},on:{pageChange:e.onPageChange}})],1),a("b-col",{attrs:{cols:"2"}},[a("add-data-btn",{staticClass:"text-end",attrs:{parent:e.parent,parentId:e.id,readOnly:e.isReadOnly,fields:e.fieldsData.list,fieldsModels:e.fieldsData.models},on:{addNewRow:e.onAddNewRow}})],1)],1):e._e()],1)],1)],1)],1)},n=[],l=a("1da1"),s=a("ade3"),r=a("5530"),o=(a("96cf"),a("b0c0"),a("2f62")),d=a("43b3"),c=a("688b"),u=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("b-row",{staticClass:"mb-4"},[a("b-col",[a("b-row",e._l(e.filtersData.model,(function(t){return a("b-col",{key:t.id,staticClass:"mb-2",attrs:{cols:"12"}},[a("router-link",{attrs:{to:{name:"dict",params:{name:t.key,title:t.multiple}}}},[a("b-button",{staticClass:"w-100"},[e._v(e._s(t.multiple))])],1)],1)})),1)],1),a("b-col",{staticClass:"text-end",attrs:{cols:"8"}},[a("b-row",e._l(e.filtersData.model,(function(t,i){return a("b-col",{key:t.id,staticClass:"mb-2",attrs:{cols:"12"}},[a("b-row",[a("b-col",{staticClass:"position-relative",attrs:{cols:"6"}},[a("label",{staticClass:"text-end lh-lg"},[e._v(e._s(t.label)+":")])]),a("b-col",[a("change-field-modal",{ref:"filter-field-"+t.key,refInFor:!0,attrs:{label:t.text,model:t.key,disabled:t.disabled,resetBtn:!0,rowId:i,items:e.getModelItems(t.key)},on:{updateField:e.onUpdateField,labelChange:e.onLabelChange,resetFilters:e.onResetFilters}})],1)],1)],1)})),1)],1)],1)},f=[],p=(a("7db0"),a("d3b7"),a("c740"),a("4de4"),a("d6cf")),h={components:{ChangeFieldModal:p["a"]},props:["filtersData"],methods:{onUpdateField:function(e){var t=e.id,a=e.fields;this.$emit("applyFilters",{id:t,fields:a})},onLabelChange:function(e){var t=e.id,a=e.model;this.$emit("filterLabelChange",{itemId:t,model:a})},onResetFilters:function(e){this.$emit("resetFilters",e)},getFieldById:function(e,t,a){return this.filtersData.list[t].find((function(t){return t.id==e}))[a]},getModelItems:function(e){var t=this,a=this.filtersData.list[e],i=this.filtersData.model.findIndex((function(t){return t.key==e}));if(0!=i){var n=this.filtersData.model[i-1].key;this.filtersData.state[n]&&""!=this.filtersData.state[n]&&(a=this.filtersData.list[e].filter((function(e){return e[n]==t.filtersData.state[n]})))}return a}}},m=h,b=a("2877"),g=Object(b["a"])(m,u,f,!1,null,null,null),v=g.exports,_=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("b-row",[a("b-col",[a("b-table",{staticClass:"text-nowrap",attrs:{id:"table",items:e.itemsData.list,fields:e.localFields,"per-page":e.perPage,"current-page":e.currentPage,busy:e.isBusy,filter:e.filter,"sort-desc":e.SDesc,"head-variant":"light",bordered:"",responsive:"","show-empty":""},on:{"update:sortDesc":function(t){e.SDesc=t},"update:sort-desc":function(t){e.SDesc=t}},scopedSlots:e._u([{key:"cell(name)",fn:function(t){return[a("name-cell",{attrs:{data:t},on:{updateField:e.onUpdateField}})]}},e._l(e.selectableFields,(function(t){return{key:"cell("+t.key+")",fn:function(i){return[a("span",{key:t.id},[a("change-field-modal",{attrs:{label:e.getFieldById(i.item[t.key],t.key,"name"),model:t.key,rowId:i.item.id,items:e.fieldsData.models[t.key]},on:{updateField:e.onUpdateField}})],1)]}}})),{key:"cell(actions)",fn:function(t){return e._l(e.itemsData.actions,(function(i){return a("span",{key:i.id},["route"==i.action?a("router-link",{attrs:{to:e.name+"/"+i.to+"/"+t.item.id}},[a("b-button",{staticClass:"mr-2"},[e._v(e._s(i.label))])],1):e._e(),"delete"==i.action?a("delete-row-btn",{attrs:{label:i.label,rowId:t.item.id},on:{deleteRow:e.onDeleteRow}}):e._e()],1)}))}},{key:"table-busy",fn:function(){return[a("div",{staticClass:"text-center my-2"},[a("b-spinner",{staticClass:"align-middle me-2"}),a("strong",[e._v("Загрузка...")])],1)]},proxy:!0}],null,!0)})],1)],1)},w=[],y=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[e.editing?a("b-input-group",{scopedSlots:e._u([{key:"append",fn:function(){return[a("b-button",{staticClass:"rounded-0",attrs:{variant:"success"},on:{click:e.changeName}},[a("b-icon",{attrs:{icon:"check"}})],1),a("b-button",{staticClass:"rounded-0 rounded-end",attrs:{variant:"danger"},on:{click:function(t){return e.showChangeInput(!1)}}},[a("b-icon",{attrs:{icon:"x"}})],1)]},proxy:!0}])},[a("b-form-input",{model:{value:e.value,callback:function(t){e.value=t},expression:"value"}})],1):a("div",{staticClass:"text"},[a("span",{staticClass:"me-2"},[e._v(e._s(e.data.value))]),a("b-icon",{staticClass:"cursor-pointer",attrs:{icon:"pencil-square"},on:{click:function(t){return e.showChangeInput(!0)}}})],1)],1)},F=[],k={props:["data"],data:function(){return{editing:!1,value:this.data.value,id:this.data.item.id}},methods:{showChangeInput:function(e){this.value=this.data.value,this.editing=e},changeName:function(){var e={field:"name",value:this.value};this.$emit("updateField",{id:this.id,fields:e}),this.editing=!1}}},C=k,D=(a("9e4c"),Object(b["a"])(C,y,F,!1,null,"481b578a",null)),x=D.exports,O=a("46c2"),I={components:{NameCell:x,ChangeFieldModal:p["a"],DeleteRowBtn:O["a"]},props:["parent","itemsData","fieldsData","isBusy","filter","perPage","currentPage","name"],data:function(){return{SDesc:!1}},computed:{localFields:function(){var e=this;return this.parent?this.fieldsData.list.filter((function(t){return t.key!=e.parent})):this.fieldsData.list},selectableFields:function(){return this.fieldsData.list.filter((function(e){return"selectable"==e.type}))}},methods:Object(r["a"])(Object(r["a"])(Object(r["a"])({},Object(o["b"])(["deleteRow"])),Object(o["d"])(["updateTableItem"])),{},{onUpdateField:function(e){var t=e.id,a=e.fields,i=a.field,n=a.value;console.log("[upd]",this.name,t,i,n),this.updateTableItem({collection:this.name,id:t,field:i,value:n})},onDeleteRow:function(e){this.deleteRow({table_name:this.name,row_id:e})},getFieldById:function(e,t,a){return this.fieldsData.models[t]?this.fieldsData.models[t].find((function(t){return t.id==e}))[a]:""}})},j=I,P=Object(b["a"])(j,_,w,!1,null,null,null),R=P.exports,M=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("b-pagination",{attrs:{"total-rows":e.rows,"per-page":e.perPage,"first-number":"","last-number":"","aria-controls":"table"},model:{value:e.currentPageLocal,callback:function(t){e.currentPageLocal=t},expression:"currentPageLocal"}})},$=[],S={props:["rows","perPage","currentPage"],data:function(){return{currentPageLocal:this.currentPage}},watch:{currentPage:function(e){this.currentPageLocal=e},currentPageLocal:function(e){this.$emit("pageChange",e)}}},L=S,E=Object(b["a"])(L,M,$,!1,null,null,null),B=E.exports,N=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[e.readOnly?a("b-button",{attrs:{variant:"primary"}},[e._v(" Импорт ")]):a("add-new-row",{attrs:{parent:e.parent,parentId:e.parentId,fields:e.fields,fieldsModels:e.fieldsModels,title:"Добавление записи"},on:{addNewRow:e.onAddNewRow}})],1)},A=[],U=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("b-button",{attrs:{variant:"primary"},on:{click:function(t){return e.showAddModal(t.target)}}},[e._v(" Добавить ")]),a("b-modal",{attrs:{id:e.addModal.id,title:e.addModal.title,centered:""},on:{hide:e.resetAddModal},scopedSlots:e._u([{key:"modal-footer",fn:function(t){var i=t.ok,n=t.cancel;return[a("b-button",{attrs:{variant:"danger"},on:{click:function(e){return n()}}},[e._v(" Отмена ")]),a("b-button",{attrs:{variant:"success"},on:{click:function(t){return e.addNewRow(i)}}},[e._v(" OK ")])]}}])},e._l(e.localFields,(function(t){return a("b-row",{key:t.id,staticClass:"py-2"},["actions"!=t.key?a("b-col",{staticClass:"position-relative d-flex align-items-center"},[a("label",{staticClass:"mb-0"},[e._v(e._s(t.label)+":")])]):e._e(),"actions"!=t.key?a("b-col",{attrs:{cols:"8"}},[t.type&&"selectable"==t.type?a("change-field-modal",{ref:"change-field-"+t.key,refInFor:!0,attrs:{label:"Не выбрано",model:t.key,rowId:"-1",items:e.fieldsModels[t.key]},on:{updateField:e.onUpdateField,labelChange:e.onLabelChange}}):t.type&&"float"==t.type?a("float-field",{attrs:{model:t.key},on:{updateField:e.onUpdateField}}):t.type&&"integer"==t.type?a("int-field",{attrs:{model:t.key},on:{updateField:e.onUpdateField}}):t.type&&"boolean"==t.type?a("boolean-field",{attrs:{model:t.key},on:{updateField:e.onUpdateField}}):t.type&&"date"==t.type?a("date-field",{attrs:{model:t.key},on:{updateField:e.onUpdateField}}):a("b-form-input",{attrs:{placeholder:"Введите текст"},model:{value:e.addModal.fields[t.key],callback:function(a){e.$set(e.addModal.fields,t.key,a)},expression:"addModal.fields[field.key]"}})],1):e._e()],1)})),1)],1)},G=[],T=(a("159b"),a("b64b"),a("54c2")),H=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("b-form-input",{attrs:{type:"number",step:"any","no-wheel":!0,placeholder:"Введите число"},model:{value:e.input,callback:function(t){e.input=t},expression:"input"}})},q=[],J={props:["model"],data:function(){return{input:""}},watch:{input:function(e){var t={field:this.model,value:e};this.$emit("updateField",{id:-1,fields:t})}}},W=J,z=Object(b["a"])(W,H,q,!1,null,null,null),K=z.exports,Q=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("b-form-input",{attrs:{type:"number",step:"1","no-wheel":!0,placeholder:"Введите целое число"},model:{value:e.input,callback:function(t){e.input=t},expression:"input"}})},V=[],X={props:["model"],data:function(){return{input:""}},watch:{input:function(e){var t={field:this.model,value:e};this.$emit("updateField",{id:-1,fields:t})}}},Y=X,Z=Object(b["a"])(Y,Q,V,!1,null,null,null),ee=Z.exports,te=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("b-form-checkbox",{attrs:{value:e.checked,"unchecked-value":e.unchecked,size:"lg"},model:{value:e.input,callback:function(t){e.input=t},expression:"input"}})],1)},ae=[],ie={props:["model"],data:function(){return{input:!1,checked:!0,unchecked:!1}},watch:{input:function(e){var t={field:this.model,value:e};this.$emit("updateField",{id:-1,fields:t})}}},ne=ie,le=Object(b["a"])(ne,te,ae,!1,null,null,null),se=le.exports,re=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("b-form-datepicker",{attrs:{placeholder:"Выберите дату",locale:"ru","hide-header":!0},model:{value:e.input,callback:function(t){e.input=t},expression:"input"}})},oe=[],de={props:["model"],data:function(){return{input:""}},watch:{input:function(e){var t={field:this.model,value:e};this.$emit("updateField",{id:-1,fields:t})}}},ce=de,ue=Object(b["a"])(ce,re,oe,!1,null,null,null),fe=ue.exports,pe={components:{ChangeFieldModal:p["a"],FloatField:K,IntField:ee,BooleanField:se,DateField:fe},props:["title","fields","fieldsModels","parent","parentId"],data:function(){return{API:new T["a"](this),addModal:{id:"add-row-modal",title:this.title,fields:{}}}},computed:{localFields:function(){var e=this;return this.parent?this.fields.filter((function(t){return t.key!=e.parent})):this.fields}},methods:{showAddModal:function(e){this.$bvModal.show(this.addModal.id,e)},resetAddModal:function(){for(var e in this.addModal.fields)this.addModal.fields[e]="",delete this.addModal.fields[e]},onLabelChange:function(e){var t=e.id,a=e.model;this.$refs["change-field-".concat(a)][0].labelReplacement=this.getFieldById(t,a,"name")},onUpdateField:function(e){e._id;var t=e.fields;this.$set(this.addModal.fields,t.field,t.value)},addNewRow:function(e){var t=this,a={};Object.keys(this.addModal.fields).forEach((function(e){a[e]=t.addModal.fields[e]})),this.parent&&(a[this.parent]=this.parentId),this.$emit("addNewRow",a),e()},getFieldById:function(e,t,a){return this.fieldsModels[t].find((function(t){return t.id==e}))[a]}}},he=pe,me=Object(b["a"])(he,U,G,!1,null,null,null),be=me.exports,ge={components:{AddNewRow:be},props:["parent","parentId","readOnly","fields","fieldsModels"],methods:{onAddNewRow:function(e){this.$emit("addNewRow",e)}}},ve=ge,_e=Object(b["a"])(ve,N,A,!1,null,null,null),we=_e.exports,ye=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[0==e.items.list.length?a("h5",[e._v("Нет доступных записей!")]):a("b-card",{staticClass:"mb-4",attrs:{header:"Выберите из списка"}},e._l(e.items.list,(function(t){return a("b-form-checkbox",{key:t.id,attrs:{checked:t.checked},on:{change:function(a){return e.changeSelection(a,t.id)}}},[e._v(" "+e._s(t.name)+" ")])})),1)],1)},Fe=[],ke={props:["items","fields","id","name"],data:function(){return{parent_id:this.id,child_table:this.fields.list[0].key,parent_table:this.fields.list[1].key}},methods:Object(r["a"])(Object(r["a"])({},Object(o["b"])(["updateSelection"])),{},{changeSelection:function(e,t){this.updateSelection({collection:this.name,parent:this.parent_table,parent_id:this.parent_id,child:this.child_table,child_id:t,value:e})}})},Ce=ke,De=Object(b["a"])(Ce,ye,Fe,!1,null,null,null),xe=De.exports,Oe=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[0==e.items.list.length?a("h5",[e._v("Нет доступных записей!")]):e._l(e.radioGroups,(function(t,i){return a("b-card",{key:i,staticClass:"mb-4",attrs:{header:"Выберите одно из списка"}},[a("b-form-group",{staticClass:"mb-0"},[a("RadioGroupElement",{attrs:{id:e.id,name:e.name,group:t,index:i,selection:e.groupSelections[i],parent:e.parent_table,child:e.child_table}})],1)],1)}))],2)},Ie=[],je=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("b-form-radio-group",{attrs:{stacked:""},on:{change:function(t){return e.changeSelection(t,e.group[e.index].work_stage)}},model:{value:e.localSelection,callback:function(t){e.localSelection=t},expression:"localSelection"}},e._l(e.group,(function(t){return a("b-form-radio",{key:t.id,attrs:{value:t.id}},[e._v(" "+e._s(t.name)+" ")])})),1)},Pe=[],Re={props:["id","name","group","index","selection","parent","child"],data:function(){return{localSelection:this.selection,prev:null,current:null}},methods:Object(r["a"])(Object(r["a"])({},Object(o["b"])(["updateRadioSelection"])),{},{changeSelection:function(e,t){console.log("[changeSelection() radio update]",e,t),this.updateRadioSelection({collection:this.name,parent:this.parent,parent_id:this.id,child:this.child,child_id:this.id,prev:this.prev,current:this.current})}}),watch:{localSelection:function(e,t){this.prev=t,this.current=e}}},Me=Re,$e=Object(b["a"])(Me,je,Pe,!1,null,null,null),Se=$e.exports,Le={props:["items","groupField","fields","id","name"],components:{RadioGroupElement:Se},data:function(){return{parent_id:this.id,parent_table:this.fields.list[0].key,child_table:this.fields.list[1].key}},computed:{radioGroups:function(){var e=[];return this.items.list.forEach((function(t){e[t.work_stage]||(e[t.work_stage]=[{id:-1,name:"Не выбрано",work_stage:t.work_stage}]),e[t.work_stage].push(t)})),e.filter(Boolean)},groupSelections:function(){for(var e=[],t=0;t<this.radioGroups.length;t++){var a=this.radioGroups[t].filter((function(e){return 1==e.checked})),i=0==a.length?-1:a[0].id;e[t]=i}return e}}},Ee=Le,Be=Object(b["a"])(Ee,Oe,Ie,!1,null,null,null),Ne=Be.exports,Ae={components:{Title:d["a"],SearchBar:c["a"],Filters:v,Table:R,Pagination:B,AddDataBtn:we,SelectGroup:xe,RadioGroup:Ne},props:["name","id","parent"],data:function(){return{searchFilter:null,perPage:10,currentPage:1,isReadOnly:!1}},computed:Object(r["a"])(Object(r["a"])({},Object(o["c"])(["title","mode","groupField","isBusy","isFiltered","itemsData","fieldsData","selectableFields","itemRowsLength","filtersData","filterParams"])),{},{compiledParams:function(){var e={};return null!==this&&void 0!==this&&this.parent&&(e=Object(s["a"])({},this.parent,this.id)),null!=this.mode&&(e["mode"]=this.mode,e["child"]=this.fieldsData.list[0].key),null!=this.groupField&&(e["child"]=this.fieldsData.list[1].key),e}}),methods:Object(r["a"])(Object(r["a"])(Object(r["a"])({},Object(o["b"])(["getItems","getFieldsModels","getFiltersItems","resetFiltersFromId","getTableInfo","applyFilters","addNewRow"])),Object(o["d"])(["updateFieldsList","resetItemsActions","updateItemsActions","resetFiltersModel","updateFiltersModel","resetFilterState","addTableItem","updateObj","updateFilterLabel"])),{},{onApplyFilters:function(e){e._id;var t=e.fields;this.applyFilters(t),this.getItems({name:[this.name],params:this.filterParams})},resetFilters:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:0;this.resetFiltersFromId(e);var t=this.compiledParams;0!=e&&(t=Object(r["a"])(Object(r["a"])({},t),this.filterParams)),this.getItems({name:[this.name],params:t})},onResetFilters:function(e){this.resetFilters(e)},onFilterChange:function(e){this.searchFilter=e},onFilterLabelChange:function(e){var t=e.itemId,a=e.model;this.updateFilterLabel({itemId:t,model:a})},onPageChange:function(e){this.currentPage=e},onAddNewRow:function(e){this.resetFilters(0),this.addNewRow({table_name:this.name,row:e})},init:function(){var e=this;return Object(l["a"])(regeneratorRuntime.mark((function t(){var a,i;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return a=function(e){var t=e.getBoundingClientRect();return t.top>=0&&t.left>=0&&t.bottom<=(window.innerHeight||document.documentElement.clientHeight)&&t.right<=(window.innerWidth||document.documentElement.clientWidth)},t.next=3,e.getTableInfo({name:e.name});case 3:e.getItems({name:e.name,params:e.compiledParams}),i=document.querySelector(".table-responsive"),null!=i&&setTimeout((function(){a(i)?(i.classList.remove("b-table-sticky-header"),i.style.maxHeight="unset"):(i.classList.add("b-table-sticky-header"),i.style.maxHeight="500px")}),500);case 6:case"end":return t.stop()}}),t)})))()}}),mounted:function(){this.init()},watch:{name:function(){this.init()}}},Ue=Ae,Ge=Object(b["a"])(Ue,i,n,!1,null,null,null);t["default"]=Ge.exports},"9e4c":function(e,t,a){"use strict";a("f97b")},f97b:function(e,t,a){}}]);
//# sourceMappingURL=dict.a6fd5113.js.map