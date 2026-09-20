"""NEXO serial response parser."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class ControllerResponse:
    category:str
    value:str
    fields:dict[str,str]

def parse_response(line:str)->ControllerResponse:
    text=line.strip()
    if "=" not in text: raise ValueError(f"Malformed NEXO response: {text!r}")
    category,payload=text.split("=",1)
    parts=payload.strip().split()
    value=parts[0] if parts else ""
    fields={}
    for part in parts:
        if "=" in part:
            key,val=part.split("=",1); fields[key.upper()]=val
    return ControllerResponse(category.strip().upper(),value,fields)
