import React,{useState,useRef,useEffect} from "react";
import Box from "@material-ui/core/Box";

function SearchBar(props){

    const [open,setOpen]=useState(false);
    const [query,setQuery]=useState("");
    //to close dropdown on clicking outside the dropdown
    const ref=useRef(null);

    useEffect(()=>{
        ["click","touchend"].forEach(e=>{
            document.addEventListener(e,toggle);
        })
        return ()=>["click","touchend"].forEach(e=>{
            document.removeEventListener(e,toggle);
        })
    },[]);

    function toggle(e){
        console.dir(e.target,ref.curent);
        setOpen(e && e.target===ref.current)
    }

    function filter(options){
        return options.filter((option)=>
                        (option.id).toLowerCase().indexOf(query.toLowerCase())>-1)
    }
    function displayValue(){
        if(query.length>0) return query
        if(props.value) return props.value.id;
        return "";
    }
    function selectOption(e){
        setQuery("");
        props.onChange(e); 
        setOpen(false)
    }
    return <Box className="dropdown">
    <Box className="control" >
    <p>Showing reasons for:-</p>
        <Box className="selected-value" >
            <input
                ref={ref}
                placeholder={props.value?props.value[props.value.id]:props.prompt}
                value={displayValue()}
                onChange={
                    e=>{
                        setQuery(e.target.value)
                        props.onChange(null)
                    }
                }
                onClick={toggle}
                onTouchEnd={toggle}
            />
        </Box>
        <Box className={`arrow ${open?"open":null}`} />
    </Box>
    <Box className={`options ${open?"open":null}`}>

    {
    filter(props.Reasons).map(e =>
     (<Box className={`option ${props.value===e?"selected":null}`} 
            onClick={()=> selectOption(e)}
            onTouchEnd={()=>selectOption(e)}
            key={e.key}> {e.id}
        </Box>))
    }
    </Box>
    </Box>
}
export default SearchBar;