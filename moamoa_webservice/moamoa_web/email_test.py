from control.policy import policy
import smtplib
from email.mime.text import MIMEText
from control.weather import weather 
from control.user_crud import User
from control.crawling import crawling



def sendMail(me, you,news,href,n,h,product,today_price,today_trade,tomorrow_price,tomorrow_trade,toto_price,toto_trade,next_price,next_trade,temp,last,temp_max,temp_min,chegam,location) :
	
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(me, '*******')

			
    html="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
<head style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
<!-- If you delete this meta tag, Half Life 3 will never be released. -->
<meta name="viewport" content="width=device-width" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
<title style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">ZURBemails</title>


<link rel="preconnect" href="https://fonts.googleapis.com" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">


<link rel="preconnect" href="https://fonts.googleapis.com" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">



</head>
 
<body bgcolor="#FFFFFF" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;-webkit-font-smoothing: antialiased;-webkit-text-size-adjust: none;height: 100%;width: 100%!important;">

<!-- HEADER -->
<table class="head-wrap" bgcolor="#FFFFFF" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
	<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
		<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"></td>
		<td class="header container" style="margin: 0 auto!important;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;display: block!important;max-width: 600px!important;clear: both!important;">
				
				<div class="content" style="margin: 0 auto;padding: 15px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 600px;display: block;">
				<table bgcolor="#FFFFFF" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
					<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
						<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"><img src="https://drive.google.com/uc?id=1qgUt_kUxvAJcX7tpmTJxpy_X4TgOWnNn" align="absmiddle" border="0" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;"></td>

					</tr>
				</table>
				</div>
		</td>
		<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"></td>
	</tr>
</table><!-- /HEADER -->


<!-- BODY -->
<table class="body-wrap" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
	<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
		<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"></td>
		<td class="container" bgcolor="#FFFFFF" style="margin: 0 auto!important;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;display: block!important;max-width: 600px!important;clear: both!important;">
			<div class="content" style="margin: 0 auto;padding: 15px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 600px;display: block;">
			<table style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
				<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
					<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"> 
						<!--그래서 얼마고?-->
						<img src="http://drive.google.com/uc?export=view&id=13FnNfu_vraQie5F1SOzzuqN6w8LYPOGU" width="285px" height="auto" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;">

						<table id="prePriceTable" style="margin: 20px 10px;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;border-collapse: separate;border-spacing: 1px;text-align: center;line-height: 1.5;border-top: 1px solid #ccc;">
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;"></td><td style="text-align: center;vertical-align: middle;margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;border-bottom: 1px solid #ccc;font-size: 100%;">어제의 가격</td><td style="text-align: center;vertical-align: middle;margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;border-bottom: 1px solid #ccc;font-size: 100%;">오늘의 가격</td><td style="text-align: center;vertical-align: middle;margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;border-bottom: 1px solid #ccc;font-size: 100%;">내일의 가격</td><td style="text-align: center;vertical-align: middle;margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;border-bottom: 1px solid #ccc;font-size: 100%;">모레의 가격</td><td width="30%" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;">다음주<br style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">오늘의 가격</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;">{variety}</td><td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;">{yesterdayPrice}</td><td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;">{todayPrice}</td><td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;">{tomorrowPrice}</td><td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;">{sandPrice}</td><td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;">{nextWeekPrice}</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
					<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
						<!-- 그래서 언제 팔아? -->
						<img src="http://drive.google.com/uc?export=view&id=1rca7fjEBok00GJn_ig7Ol3DyWH9Saf99" width="330px" height="auto" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;">
						<table id="preVolumeTable" style="margin: 20px 10px;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;border-collapse: separate;border-spacing: 1px;text-align: left;line-height: 1.5;border-top: 1px solid #ccc;">
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;">오늘은 {variety}의 거래량이 {todaySell}</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;">내일은 {variety}의 거래량이 {tomorrowSell}</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;">이번주는 {variety}의 거래량이 {thisWeekSell}</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 300px;vertical-align: top;border-bottom: 1px solid #ccc;font-size: 100%;">{predictSellDay}부터 {variety}의 거래량이 {progress}</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
					<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
						<!-- 그래서 어디서 팔아? -->
						<img src="http://drive.google.com/uc?export=view&id=1MjuvfTXYPCHthfMXZk7QTqwSRp8LDTVX" width="360px" height="auto" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;">
						<table style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="border-bottom: solid 1px #ccc;margin: 20px 10px;padding: 10px;vertical-align: top;font-size: 140%;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">{location}의 추천 로컬푸드 직판장</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 20px 10px;padding: 5px 5px 5px 20px;vertical-align: top;font-size: 120%;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">{localMarketName}</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 20px 10px;padding: 5px 5px 5px 35px;vertical-align: top;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">전화번호 : {localMarketPhone}</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 20px 10px;padding: 5px 5px 5px 35px;vertical-align: top;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">주소 : {localMarketlocate}</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 20px 10px;padding: 5px 5px 5px 35px;vertical-align: top;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">나와의 거리 : {localMarketDistance}</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 20px 10px;padding: 5px 5px 35px 35px;vertical-align: top;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">예상 소요 유류비 : {localMarketOilPrice}</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="font-size: 120%;width: 80%;text-align: center;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
									얼마나 팔아야 "가락시장"보다 비싸게 팔 수 있는지 궁금하다면? >>
								</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="text-align: center;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
									<a href="{toCalcPage}" id="showDetailPage" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;text-decoration: none;">
									<img src="http://drive.google.com/uc?export=view&id=1INLAPax926nBMsB8A7Hqc_cgnTWbur8n" width="120px" height="auto;" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;">
									</a>
									<a href="{toDetailPage}" id="showDetailPage" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;text-decoration: none;">
									<img src="http://drive.google.com/uc?export=view&id=1_AQ_41PXfvweATgnj6z5iwKWENu92FdY" width="120px" height="auto;" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;">
									</a>
								</td>
							</tr>
						</table>
					</td>
				</tr><tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
					<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
						<!-- 슬기로운 마을의 날씨 -->
						<img src="http://drive.google.com/uc?export=view&id=1fONjEpPl1vJMNsUaRsLz6GrwPzka6Jb3" style="margin: 20px 0px;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;" width="390px" height="auto">
						<table style="text-align: center;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
									<img src="{weatherImgSrc}" style="margin: 20px;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;" width="200px" height="auto">
								</td>
							</tr>
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td style="border-left: 1px solid #ccc;padding: 10px;vertical-align: top;margin: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">{location} 날씨 : {todayWeather}</td>
								<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"></td><td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"></td><td class="tempList" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;border-right: 1px solid #ccc;text-align: center;"></td>
							</tr>
						</table>
						<table style="text-align: center;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;">
							<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
								<td class="tempList" style="border-left: 1px solid #ccc;margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;border-right: 1px solid #ccc;text-align: center;">기온 : {temperature}</td>
								<td class="tempList" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;border-right: 1px solid #ccc;text-align: center;">최고기온 : {maxTemp}</td>
								<td class="tempList" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;border-right: 1px solid #ccc;text-align: center;">최저기온 : {minTemp}</td>
								<td class="tempList" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;border-right: 1px solid #ccc;text-align: center;">체감기온 : {chegam}</td>
							</tr>
						</table>

					</td>
				</tr>
				<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
					<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
						<!-- 오늘의 HOT 뉴스 -->
						<img src="http://drive.google.com/uc?export=view&id=1ERT7UKNXtU8OBMaZhOTPa-EEH3mXxulP" style="margin: 20px 0px 0px 0px;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;" width="320px" height="auto">
						<table id="newsTable" style="margin: 20px 10px;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;border-collapse: collapse;text-align: left;line-height: 1.5;border-top: 1px solid #ccc;border-bottom: 1px solid #ccc;">
							<tr style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 150px;vertical-align: top;">
								<td class="newsPolicyNum" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 10%;vertical-align: top;color: black;">
									<h4 style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 500;font-size: 23px;">1.</h4>
								</td>
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;color: black;">
									<a href="http://www.ikpnews.net/{news1url}" style="color: #000;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;text-decoration: none;">{news1}</a>
								</td>
							</tr>
							<tr style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 150px;vertical-align: top;">
								<td class="newsPolicyNum" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 10%;vertical-align: top;color: black;">
									<h4 style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 500;font-size: 23px;">2.</h4>
								</td>
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;color: black;">
									<a href="http://www.ikpnews.net/{news2url}" style="color: #000;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;text-decoration: none;">{news2}</a>
								</td>
							</tr>
							<tr style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 150px;vertical-align: top;">
								<td class="newsPolicyNum" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 10%;vertical-align: top;color: black;">
									<h4 style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 500;font-size: 23px;">3.</h4>
								</td>
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;color: black;">
									<a href="http://www.ikpnews.net/{news3url}" style="color: #000;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;text-decoration: none;">{news3}</a>
								</td>
							</tr>
							<tr style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 150px;vertical-align: top;">
								<td class="newsPolicyNum" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 10%;vertical-align: top;color: black;">
									<h4 style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 500;font-size: 23px;">4.</h4>
								</td>
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;color: black;">
									<a href="http://www.ikpnews.net/{news4url}" style="color: #000;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;text-decoration: none;">{news4}</a>
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
					<td style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
						<!-- 이게 무슨 정책이야? -->
						<img src="http://drive.google.com/uc?export=view&id=1HhUgOTr0Od6EvGsJsKG8efEfkE6PFMuD" width="390px" height="auto" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;">
						<table id="policyTable" style="margin: 20px 10px;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 100%;border-collapse: collapse;text-align: left;line-height: 1.5;border-top: 1px solid #ccc;border-bottom: 1px solid #ccc;">
							<tr style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 150px;vertical-align: top;">
								<td class="newsPolicyNum" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 10%;vertical-align: top;color: black;">
									<h4 style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 500;font-size: 23px;">1.</h4>
								</td>
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;color: black;">
									<a href="https://www.nongmin.com/{policy1url}" style="color: #000;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;text-decoration: none;">{policy1}</a>
								</td>
							</tr>
							<tr style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 150px;vertical-align: top;">
								<td class="newsPolicyNum" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 10%;vertical-align: top;color: black;">
									<h4 style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 500;font-size: 23px;">2.</h4>
								</td>
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;color: black;">
									<a href="https://www.nongmin.com/{policy2url}" style="color: #000;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;text-decoration: none;">{policy2}</a>
								</td>
							</tr>
							<tr style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 150px;vertical-align: top;">
								<td class="newsPolicyNum" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 10%;vertical-align: top;color: black;">
									<h4 style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 500;font-size: 23px;">3.</h4>
								</td>
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;color: black;">
									<a href="https://www.nongmin.com/{policy3url}" style="color: #000;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;text-decoration: none;">{policy3}</a>
								</td>
							</tr>
							<tr style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 150px;vertical-align: top;">
								<td class="newsPolicyNum" style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;width: 10%;vertical-align: top;color: black;">
									<h4 style="margin: 0;padding: 0;font-family: &quot;HelveticaNeue-Light&quot;, &quot;Helvetica Neue Light&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Lucida Grande&quot;, sans-serif;line-height: 1.1;margin-bottom: 15px;color: #000;font-weight: 500;font-size: 23px;">4.</h4>
								</td>
								<td style="margin: 0;padding: 10px;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;vertical-align: top;color: black;">
									<a href="https://www.nongmin.com/{policy4url}" style="color: #000;margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;text-decoration: none;">{policy4}</a>
								</td>
							</tr>
						</table>
					
					</td>
				</tr>
				<tr style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;">
					<td align="center" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;"> <!-- 슬기로운 농부생활 메인페이지로 이어지는 버튼 -> url 수정 필요 -->
						<a href="{toMainPage}" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;text-decoration: none;">
							<img src="http://drive.google.com/uc?export=view&id=1jHm6DpboFIEsWYrqS9shsV0_2BQtrVyC" width="300" height="auto;" style="margin: 0;padding: 0;font-family: &quot;Helvetica Neue&quot;, &quot;Helvetica&quot;, Helvetica, Arial, sans-serif;max-width: 100%;">
						</a>
					</td>
				</tr>
			</table>
	</div></td></tr>
</table><!-- /BODY -->

</body>
</html>
    """.format(variety = product, yesterdayPrice=9400, todayPrice=today_price, tomorrowPrice =tomorrow_price, sandPrice =toto_price, nextWeekPrice =next_price, \
		toDetailPage = 'http://f432-115-138-113-134.ngrok.io/moa/no_subcribe' , toCalcPage = 'http://f432-115-138-113-134.ngrok.io/moa/minicalc', toMainPage='http://f432-115-138-113-134.ngrok.io/moa/no_subcribe',\
		news1url = h[0], news1=n[0], news2=n[1], news2url=h[1], news3=n[2], news3url=h[2], news4=n[3], news4url=h[3], \
		policy1url=href[0], policy1 = news[0], policy2url=href[1], policy2 = news[1], policy3url=href[2], policy3=news[2], policy4url=h[3], policy4=news[3], \
		tomorrowVolume = "", thisWeekVolume = "", nextWeekVolume = "",\
		weatherImgSrc = "",\
		location=location, todayWeather = last, temperature = temp, \
		maxTemp =temp_max, minTemp = temp_min, chegam = chegam, \
		localMarketName = "가창농협로컬푸드직매장", localMarketPhone = "053-767-8568", localMarketlocate = "대구 달성군 기장면", localMarketDistance ="88km", localMarketOilPrice = "142912원", \
		todaySell = "내려갔습니다", tomorrowSell = "어제와 비슷합니다", thisWeekSell = "어제보다 오릅니다", predictSellDay = "다음주부터", progress = "내려갈것으로 예상됩니다.")

    part2 = MIMEText(html, 'html')
	
    smtp.sendmail(me, you, part2.as_string())
    smtp.quit()


news,href=policy()
n,h =crawling()
get = User.all_email()
email_list=[]
for i in get:
    email_list.append(i[0])

product_list=[]
location_list=[]
y_price=[]
for k in email_list:
    	product_list.append(User.get_product(k))
		

		
for y in email_list:
		location_list.append(User.get_location(y)[0])

predict_list=[]
for j in product_list:
	predict_list.append(j[0])

for i in range(2):
    temp,last,temp_min,temp_max,chegam,mise = weather(location_list[i])
    pre=User.predict(predict_list[i])
    sendMail('********', email_list[i],news,href,n,h,pre[0][0],pre[0][1],pre[0][2],pre[0][3],pre[0][4],pre[0][5],pre[0][6],pre[0][7],pre[0][8],temp,last,temp_max,temp_min,chegam,location_list[i])


