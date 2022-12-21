
*** Settings ***
Documentation       Template robot main suite.
Library    Process
Library    Collections
Library    OperatingSystem

*** Keywords ***
Run shell command
    [Arguments]    ${command}    ${timeout}
    ${result}=      Run Process     
    ...    ${command}
    ...    shell=True
    ...    stdout=${CURDIR}${/}stdout.log
    ...    stderr=STDOUT
    ...    cwd=${CURDIR}
    ...    timeout=${timeout}   
    [Return]    ${result.stdout}

RCC Diagnostics
    ${result}=    Run shell command    rcc config diagnostics    10s
    Log   ${result} 

Check Proxy Settings
    ${result}=    Run shell command    netsh winhttp show proxy    10s
    Log   ${result} 

Requests Help
    ${result}=    Run shell command    python -m requests.help    10s
    Log   ${result} 

TLS Test to Robocorp Vault
    ${result}=    Run shell command    python task_robocorp_vault.py    10s
    Log   ${result} 

TLS test to US instance
    ${result}=    Run shell command    python task_generic_request.py US    10s
    Log   ${result} 

TLS test to EU instance
    ${result}=    Run shell command    task_generic_request.py    10s
    Log   ${result} 

TLS test OpenSSL direct
    ${result}=    Run shell command    openssl s_client -connect api.us1.robocorp.com:443 -prexit -showcerts    10s
    Log   ${result} 

*** Tasks ***
Run Network Diagnostics
    RCC Diagnostics
    Check Proxy Settings
    Requests Help
    TLS test OpenSSL direct
    TLS test to EU instance
    TLS test to US instance
    [Teardown]    Remove File    ${CURDIR}${/}stdout.log