window.onload = function() {
    const osElems = document.querySelectorAll(".tab-title-os")
    osElems.forEach(elem => elem.onclick=showOs)
    
    const langElems = document.querySelectorAll(".tab-title-lang")
    langElems.forEach(elem => elem.onclick=showLang)
    
    const ideElems = document.querySelectorAll(".tab-title-ide")
    ideElems.forEach(elem => elem.onclick=showIde)

    const tabs = document.querySelectorAll(".tab");
    tabs.forEach(tab => {
        for (elem of tab.children) {
            if(elem.className != "tab-title"){
                elem.className="hidden";
            }
        }
        tab.onclick = showContent;
    });
};

const showContent = function(){
    const elems = this.children;
    for (elem of elems){
        if(elem.className == "hidden"){
            elem.className = "active";
        } else if(elem.className == "active"){
            elem.className = "hidden";
        }
    }
}

const showOs = function() {
    const contentContainer = document.getElementsByClassName("os-content");
    for(elem of contentContainer){
        if(!elem.classList.contains("hidden")){
            elem.classList.add("hidden")
        }
    }
    const os = event.target.getAttribute("data-os-type");
    const contentElement = document.getElementsByClassName(os);
    contentElement[0].classList.remove("hidden")
};

const showLang = function() {
    const contentContainer = document.getElementsByClassName("lang-content");
    for(elem of contentContainer){
        if(!elem.classList.contains("hidden")){
            elem.classList.add("hidden")
        }
    }
    const lang = event.target.getAttribute("data-lang-type");
    const contentElement = document.getElementsByClassName(lang);
    contentElement[0].classList.remove("hidden")
};

const showIde = function() {
    const contentContainer = document.getElementsByClassName("ide-content");
    for(elem of contentContainer){
        if(!elem.classList.contains("hidden")){
            elem.classList.add("hidden")
        }
    }
    const ide = event.target.getAttribute("data-ide-type");
    const contentElement = document.getElementsByClassName(ide);
    contentElement[0].classList.remove("hidden")
};
