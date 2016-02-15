# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from octoprint.filemanager.destinations import FileDestinations

class AutoselectPlugin(octoprint.plugin.EventHandlerPlugin):
	def on_event(self, event, payload):
		if event != "Upload":
			return

		if not self._printer.is_ready():
			self._logger.debug("Printer is not ready, not autoprinting uploaded file")
			return

		filename = payload["file"]
		target = payload["target"]

		if target == FileDestinations.SDCARD:
			path = filename
			sd = True
		else:
			path = self._file_manager.path_on_disk(target, filename)
			sd = False

		self._logger.info("Selecting and printing {} on {} that was just uploaded".format(filename, target))
		self._printer.select_file(path, sd, False)
		self._printer.start_print()

__plugin_name__ = "AutoPrint Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = AutoPrintPlugin()
