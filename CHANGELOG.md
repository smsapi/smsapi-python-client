# Changes

## 2.9.6
- fix for python 3.12 - re.compile SyntaxWarning
---

## 2.9.5
- fix examples
- support "without_prefix" parameter in account API `user` method
---

## 2.9.4
- fix module name typo
---

## 2.9.3
- update API HTTP methods
---

## 2.9.2
- fix: wrong parameter passed to DELETE scheduled SMS,MMS,VMS API endpoints
---

## 2.9.1
- fix broken contacts API endpoints
---

## 2.9.0
- introduce MFA module
---

## 2.8.0
- remove push API
---

## 2.7.0
- support MFA API
- increase requests timeout to 30 seconds
---

## 2.6.0
- Support for smsapi.bg
___

## 2.5.0
- Add support for optional `details` param in SMS API, so it makes fields like (`message`, `parts`, `length`) accessible through response model. 
___

## 2.4.5

- make exceptions pickleable
___

## 2.4.4

- fix: accept 'domain' parameter from short_url API   
___

## 2.4.3

- accept 'from' parameter in sms send method   
___

## 2.4.2

- Change sms send http method to POST