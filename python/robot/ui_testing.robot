*** Settings ***
Library           Selenium2Library

*** Variables ***
${Username}       admin
${Password}       admin
${Browser}        Firefox
${SiteUrl}        https://13.127.198.209:5000/login
${DashboardTitle}   PolyLogyx - Dashboard 
${Delay}          2s

*** Test Cases ***
LoginTest
    Open Browser to the Login Page
    Enter User Name
    Enter Password
    Click Login
    sleep    ${Delay}
    Assert Dashboard Title
    Excutable path Dashboard
	Locate pie chart elements based on different colors
    sleep    ${Delay}
    [Teardown]    Close Browser

	
*** Keywords ***
Open Browser to the Login Page
    open browser    ${SiteUrl}    ${Browser}
    Maximize Browser Window

Enter User Name
    Input Text    username   ${Username}

Enter Password
    Input Text    password    ${Password}

Click Login
    click button    Sign In

Assert Dashboard Title
	${Dashb}  get title   
	Should Be Equal  ${Dashb}   ${DashboardTitle}
Excutable path Dashboard
	Click Element   xpath=//*[@id="dashboard"]
	Click Element   xpath=//*[@id="otx_counter"]
	Click Element   xpath=//*[@id="dashboard"]
	
	Click Element   xpath=//*[@id="dashboard"]
	Click Element 	xpath=//*[@id="ibm_counter"]
	sleep    ${Delay}
	Click Element   xpath=//*[@id="dashboard"]
   	Click Element	xpath=//*[@id="rule_counter"]
	sleep    ${Delay}
	Click Element   xpath=//*[@id="dashboard"]
	Click Element	xpath=//*[@id="vt_counter"]
	sleep    ${Delay}
Locate pie chart elements based on different colors
	${p}=  driver.findElement(By.xpath("//*[@id="pie-chart-platform-count"]"))
	Log To Console   ${p}
	sleep    ${Delay}
	Click Element	//*[@id="pie-chart-platform-count"]
	sleep    ${Delay}
	Click Element	//*[@id="pie-chart-platform-count"]
	sleep    ${Delay}
  
