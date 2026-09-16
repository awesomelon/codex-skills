let tenant = "alpha";
export function currentTenant() { return tenant; }
export function switchTenant(value) { tenant = value; }
