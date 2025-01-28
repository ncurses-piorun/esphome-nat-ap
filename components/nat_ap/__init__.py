
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_SSID, CONF_PASSWORD

nat_ap_ns = cg.esphome_ns.namespace('nat_ap')
NatAp = nat_ap_ns.class_('NatAp', cg.Component)

def validate_password(value):
    value = cv.string_strict(value)
    if not value:
        return value
    if len(value) < 8:
        raise cv.Invalid("WPA password must be at least 8 characters long")
    if len(value) > 64:
        raise cv.Invalid("WPA password must be at most 64 characters long")
    return value

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(NatAp),
    cv.Required(CONF_SSID): cv.ssid,
    cv.Required(CONF_PASSWORD): validate_password,
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    
    cg.add(var.set_ssid(config[CONF_SSID]))
    cg.add(var.set_password(config[CONF_PASSWORD]))
