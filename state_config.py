"""
State configuration for this OklahomaDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "OK"
STATE_NAME = "Oklahoma"
APP_NAME = "OklahomaDischargeWatch"
APP_TAGLINE = "Oklahoma Discharge Monitoring"
DOMAIN = "oklahomadischargewatch.org"
DATA_FILE = "ok_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@oklahomadischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "CST"
EPA_REGION = 6
