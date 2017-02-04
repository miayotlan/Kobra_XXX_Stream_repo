################################################################################
#                                                                              #
#                         Copyright (C) 2017 Kobra                             #
#                                                                              #
#  This Program is free software; you can darkredistribute it and/or modify    #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#      Thanks to Surfacingx, ][NT3L][G3NC][, WHUFCLEE, Midraal, OpenELEQ       #
#                                                                              #
################################################################################


import os 
import time
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import sys
import shutil
import platform
import subprocess
import urllib
import urllib2
import re

import downloader, extract, vfs
from vfs import VFSClass

X				= xbmc.executebuiltin
T				= time.sleep
KOBRA			= "[COLOR darkred][B][I]KOBRA [/I][/B][/COLOR][COLOR ghostwhite] [B]XXX STREAM AUTO INSTALLER[/B][/COLOR]"
ADDON_ID		= 'script.a.xxxstream'
ADDON			= xbmcaddon.Addon(ADDON_ID)
DIALOG			= xbmcgui.Dialog()
DP				= xbmcgui.DialogProgress()
HOME			= xbmc.translatePath('special://xbmc/media')
HOME2			= xbmc.translatePath('special://home')
ADDONS			= os.path.join(HOME, 'addons')
PACKAGES		= os.path.join(ADDONS, 'packages')
URL				= 'http://kobracustombuilds.com/adult/music/adultmusic.txt'
URL2			= 'http://kobracustombuilds.com/adult/build/xxxwizard/installxxx.txt'
USER_AGENT		= 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
INSTALLED		= ADDON.getSetting('installed')
INSTALLED2		= ADDON.getSetting('installed2')

def openURL(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', USER_AGENT)
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link


def install_mp3(version, url):
		X("PlayMedia(special://xbmc/media/notify.wav)")
		DP.create('[COLOR darkred][I][B]DOWNLOADING[/B][/I][/COLOR][COLOR ghostwhite]  [B]ADDITIONAL DATA[/B][/COLOR]',' ','',' ')
		lib=os.path.join(HOME, 'xxx.mp3')
		try: os.remove(lib)
		except: pass
		T(1)
		downloader.download(url, lib, DP)
		T(2)
		T(1)
		DP.close()
		ADDON.setSetting('installed', version)
		X('Notification([COLOR darkred][I][B]KOBRA[/B][/I][/COLOR][COLOR ghostwhite]  [B]XXX STREAM AUTO INSTALLER[/B][/COLOR],[COLOR ghostwhite]DATA DOWNLOAD COMPLETE[/COLOR],4000,special://xbmc/addons/skin.re-touched/media/kobra.png)')
		T(4)



def install_build(version, url):
	T(2)
	X("PlayMedia(special://xbmc/media/notify.wav)")
	if DIALOG.yesno(KOBRA,"[COLOR darkred]TERMS AND CONDITIONS[/COLOR][CR][COLOR ghostwhite]YOU MUST BE 18 OR OVER TO ACCESS THIS APPLICATION! BEFORE PROCEEDING YOU MUST READ AND AGREE TO THE TERMS BELOW. THE MATERIALS AVAILABLE WITHIN THIS APPLICATION INCLUDE GRAPHIC VISUAL DEPICTIONS AND DESCRIPTIONS OF NUDITY AND SEXUAL ACTIVITY. BY CLICKING I AGREE BELOW, YOU ARE AGREEING TO THE FOLLOWING: 1. YOU ARE AN ADULT, AT LEAST 18 YEARS OF AGE, YOU ARE FAMILIAR WITH AND UNDERSTAND THE STANDARDS AND LAWS OF YOUR LOCAL COMMUNITY REGARDING SEXUALLY-ORIENTED MEDIA. YOU REPRESENT THAT, BASED ON YOUR FAMILIARITY WITH THE STANDARDS AND LAWS OF YOUR LOCAL COMMUNITY, YOU WILL NOT BE VIOLATING ANY APPLICABLE STANDARDS OR LAWS BY REQUESTING, RECEIVING, DOWNLOADING OR POSSESSING ANY OF THE VIDEO, AUDIO, GRAPHICS, IMAGES OR TEXT ADULT MATERIAL AVAILABLE ON THIS APPLICATION. 2. YOU HEREBY ACKNOWLEDGE THAT ANY USE OF THIS APPLICATION IS AT YOUR SOLE RISK. YOU UNDERSTAND THAT BY ACCEPTING THE TERMS OF THIS AGREEMENT, YOU ARE AGREEING TO HOLD THE PUBLISHER OF THIS APPLICATION HARMLESS FROM ANY RESPONSIBILITIES OR LIABILITIES RELATED TO YOUR USE OF THIS APPLICATION AND THE ADULT MATERIAL CONTAINED HEREIN. 3. YOU WILL NOT PERMIT ANY PERSON(S) UNDER 18 YEARS OF AGE TO HAVE ACCESS TO ANY OF THE ADULT MATERIALS CONTAINED IN THIS APPLICATION. 4. YOU ARE VOLUNTARILY CHOOSING TO ACCESS THIS APPLICATION, BECAUSE YOU WANT TO VIEW, READ OR HEAR THE VARIOUS ADULT MATERIALS THAT ARE AVAILABLE. YOU AGREE TO IMMEDIATELY EXIT FROM THIS APPLICATION IF YOU ARE IN ANY WAY OFFENDED BY THE SEXUAL NATURE OF ANY ADULT MATERIAL. 5. IF YOU USE THIS APPLICATION IN VIOLATION OF THESE TERMS, OR USE THIS APPLICATION WHERE SUCH USE IS ILLEGAL, YOU MAY BE IN VIOLATION OF LOCAL AND/OR FEDERAL LAWS. YOU AGREE THAT YOU ARE SOLELY RESPONSIBLE FOR YOUR USE OF THIS APPLICATION AND ANY LINKED THIRD PARTY WEB SITES, AND AGREE TO INDEMNIFY PUBLISHER AGAINST ANY CLAIMS ARISING OUT OF SUCH USE. 6. BY CLICKING I AGREE AT THE BOTTOM OF THIS WINDOW OR BY ENTERING THE APPLICATION, YOU AGREE TO ABIDE BY THE COMPLETE TERMS AND CONDITIONS OF USE OF THIS APPLICATION. IF YOU DO NOT AGREE TO THE COMPLETE TERMS AND CONDITIONS OF USE, CLICK ON THE NO BUTTON TO EXIT THE APPLICATION.[/COLOR]","",""," "," "):
		DP.create('[COLOR darkred][B][I]KOBRA [/I][/B][/COLOR][COLOR ghostwhite] [B]XXX STREAM AUTO INSTALLER[/B][/COLOR]','[CR][COLOR ghostwhite]DOWNLOADING BUILD[/COLOR]','', '[COLOR dodgerblue]PLEASE WAIT[/COLOR]')
		lib=os.path.join(HOME, 'adultbuild.zip')
		DP.create(KOBRA,"[COLOR ghostwhite][CR]SEARCHING FOR DEVICE",'', "PLEASE WAIT[/COLOR]")
		try: os.remove(lib)
		except: pass
		T(3)
		X("PlayMedia(special://xbmc/media/alert.mp3)")
		DP.update(0,"", "[COLOR orange]AMAZON [/COLOR][COLOR ghostwhite]FIRE STICK DETECTED[/COLOR]")
		T(3)
		DP.update(0,"", "[COLOR ghostwhite]THIS DEVICE WILL SELF DESTRUCT IN[/COLOR]")
		T(3)
		DP.update(0,"", "[COLOR ghostwhite]3[/COLOR]")
		T(1)
		DP.update(0,"", "[COLOR ghostwhite]2[/COLOR]")
		T(1)
		DP.update(0,"", "[COLOR ghostwhite]1[/COLOR]")
		T(1)
		X("PlayMedia(special://xbmc/media/explode.mp3)")
		T(3)
		DP.update(0,"", "[COLOR ghostwhite]ONLY KIDDING HAHA[/COLOR]")
		T(2)
		DP.update(0,"", "[COLOR ghostwhite]LETS ROCK N ROLL![/COLOR]")
		X("PlayMedia(special://xbmc/media/xxx.mp3)")
		T(2)
		downloader.download(url, lib, DP)
		addonfolder = xbmc.translatePath(os.path.join('special://','home'))
		DP.update(0,"[CR][COLOR ghostwhite]INSTALLING KOBRA XXX STREAM[/COLOR]", "")
		T(3)
		DP.update(0,"", "[COLOR ghostwhite]STAY RIGHT THERE. I'LL BE BACK![/COLOR]")
		extract.all(lib,addonfolder,DP)
		DP.update(0,"[CR][COLOR ghostwhite]I TOLD YOU I'LL BE BACK!", "ALL DONE. INSTALLATION COMPLETE[/COLOR]")
		T(4)
		os.remove(lib)
		DP.close()
		DIALOG.ok(KOBRA, "[COLOR ghostwhite][CR][CR]DON'T WATCH TOO MUCH PORN![/COLOR]")
		DIALOG.ok(KOBRA, "[COLOR ghostwhite][CR]OR THE ONLY WAY YOU'LL EVER GET LAID IS IF YOU CRAWL UP A CHICKEN'S ASS AND WAIT.[CR]^^^^^^^^^^^^^^^^^^^^^^[CR]^^^^^^^^^^^^^^^^^^^^[CR]^^^^^^^^^^^^^^^^^^[CR]^^^^^^^^^^^^^^^^[CR]^^^^^^^^^^^^^^[CR]^^^^^^^^^^^^[CR]^^^^^^^^^^[CR]^^^^^^^^[CR]^^^^^^[CR]^^^^[CR]^^[CR]^[CR]BWOK BWOK BWOK BWOK-AHHHHH![/COLOR]")
		DIALOG.ok(KOBRA, "[COLOR ghostwhite][CR]WE NOW NEED TO FORCE STOP KOBRA XXX STREAM TO COMPLETE THE INSTALLATION. PLEASE RESTART THE APPLICATION. CLICK OK TO CONTINUE[/COLOR]")
		DIALOG.ok(KOBRA, '[COLOR ghostwhite]JUST ONE MORE THING BEFORE YOU GO.[CR]AN OLD MAN AND AN OLD LADY ARE GETTING READY FOR BED ONE NIGHT WHEN ALL OF A SUDDEN THE WOMAN BURSTS OUT OF THE BATHROOM, FLINGS OPEN HER ROBE AND YELLS "SUPER PUSSY!" THE OLD MAN SAYS "I WILL HAVE THE SOUP."[CR][CR]HAHAHAHA! [CR][CR]CLICK OK TO EXIT[/COLOR]')
		ADDON.setSetting('installed2', version)
		os._exit(1)
	DIALOG.ok(KOBRA, '[COLOR ghostwhite]WELL WELL WELL, I DID NOT EXPECT TO SEE YOU HERE. MAYBE IT COULD HAVE BEEN A USER ERROR.[CR] ANYWAY, A QUICK JOKE BEFORE YOU GO.[CR]AN OLD MAN AND AN OLD LADY ARE GETTING READY FOR BED ONE NIGHT WHEN ALL OF A SUDDEN THE WOMAN BURSTS OUT OF THE BATHROOM, FLINGS OPEN HER ROBE AND YELLS "SUPER PUSSY!" THE OLD MAN SAYS "I WILL HAVE THE SOUP."[CR][CR]HAHAHAHA! [CR][CR]CLICK OK TO EXIT[/COLOR]')
	X("PlayMedia(special://xbmc/media/out.wav)")

def check_mp3():
	vfs = VFSClass()
	#mod = vfs.read_file('special://home/addons/script.a.xxxstream/resources/mod.txt') # for use on standard script
	mod = vfs.read_file('special://xbmc/addons/script.a.xxxstream/resources/mod.txt') # for use on built in script on Android and Windows Application
	xbmc.log(mod)
	T(1)
	link = openURL(URL).replace('\n','').replace('\r','').replace('\t','')
	match = re.compile('name="adultmp3".+?ersion="(.+?)".+?rl="(.+?)"').findall(link)
	if len(match) > 0:
		for version, url in match:
			if version > INSTALLED:
				install_mp3(version, url)
			else: 
				xbmc.log("KOBRA XXX MP3 DOWNLOAD: No new mp3 avaliable.")
	else:
		xbmc.log("KOBRA XXX MP3 DOWNLOAD: Unable to grab mp3.", xbmc.LOGDEBUG)


def check_build():
	T(1)
	link = openURL(URL2).replace('\n','').replace('\r','').replace('\t','')
	match = re.compile('name="installxxx".+?ersion="(.+?)".+?rl="(.+?)"').findall(link)
	if len(match) > 0:
		for version, url in match:
			if version > INSTALLED2:
				install_build(version, url)
			else: 
				xbmc.log("KOBRA XXX BUILD DOWNLOAD: No new zip avaliable.")
	else:
		xbmc.log("KOBRA XXX BUILD DOWNLOAD: Unable to grab zip.", xbmc.LOGDEBUG)


if (__name__ == "__main__"):
	check_mp3()
	check_build()