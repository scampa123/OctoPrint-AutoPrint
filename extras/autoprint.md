---
layout: plugin

id: autoselect
title: OctoPrint-AutoPrint
description: Automatically selects and prints freshly uploaded files for printing if no print job is currently active.
author: Gina Häußge and Sal Campana
license: AGPLv3

date: 2016-02-14

homepage: https://github.com/scampa123/OctoPrint-AutoPrint
source: https://github.com/scampa123/OctoPrint-AutoPrint
archive: https://github.com/scampa123/OctoPrint-AutoPrint/archive/master.zip

tags:
- ux
- upload
- filemanagement

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.0
---

The AutoPrint Plugin will automatically select newly uploaded files for
printing if there is an active connection to a printer and currently no print
job running.
