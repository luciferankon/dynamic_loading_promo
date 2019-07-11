window.onload = function() {
    const osElems = document.querySelectorAll(".tab-title-os")
    osElems.forEach(elem => elem.onclick=showOs)
    
    const langElems = document.querySelectorAll(".tab-title-lang")
    langElems.forEach(elem => elem.onclick=showLang)
    
    const ideElems = document.querySelectorAll(".tab-title-ide")
    ideElems.forEach(elem => elem.onclick=showIde)

    const osOptions = document.querySelectorAll(".os_option");
    const langOptions = document.querySelectorAll(".lang_option");
    const ideOptions = document.querySelectorAll(".ide_option");

    osOptions.forEach(option => (option.onclick = showOs));
    langOptions.forEach(option => (option.onclick = showLang));
    ideOptions.forEach(option => (option.onclick = showIde));
};

const showOs = function() {
    const contentContainer = document.getElementById("os-content");
    for(elem of contentContainer.children){
        if(!elem.classList.contains("hidden")){
            elem.classList.add("hidden")
        }
    }
    const os = event.target.getAttribute("data-os-type");
    const contentElement = document.getElementById(os + "-content");
    contentElement.classList.remove("hidden")
};

const showLang = function() {
    const contentContainer = document.getElementById("lang-content");
    for(elem of contentContainer.children){
        if(!elem.classList.contains("hidden")){
            elem.classList.add("hidden")
        }
    }
    const lang = event.target.getAttribute("data-lang-type");
    const contentElement = document.getElementById(lang + "-content");
    contentElement.classList.remove("hidden")
};

const showIde = function() {
    const contentContainer = document.getElementById("ide-content");
    for(elem of contentContainer.children){
        if(!elem.classList.contains("hidden")){
            elem.classList.add("hidden")
        }
    }
    const ide = event.target.getAttribute("data-ide-type");
    const contentElement = document.getElementById(ide + "-content");
    contentElement.classList.remove("hidden")
};
