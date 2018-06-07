"""
    There you are, writing your Python code like a boss, your screen looking
    like a poster for Matrix, when suddenly you find yourself in need to send
    an email. :email: What do you do? Surely you won't open Outlook,
    that would totally ruin your command-line-based setup.. No, you're gonna
    use the ga_tools module to send your email via the command line!
    (It's also very useful for sending automated emails with the reports that
    your scripts create, but that clearly isn't as cool.)

    The emails get sent from "benchmark@eighty-days.com". If you want to use
    your own email, just pass your email as an "email" argument, and your
    password as a "password" argument. Be cautious not to write the passwords
    into any files that you might be sharing in the future!

    https://80days.github.io/benchmark-tools/ga_tools#emails
"""
from eighty_tools.ga_tools import send_email

send_email(
	to="jan.morawiec@eighty-days.com",
	subject="Please Stop",
	html="""
	Dear Jan,<br>
	The comments for your code snippets are both unprofessional and not funny.<br>
	<b>PLEASE STOP</b><br>
	Thanks,<br>
	Everyone in this channel
	""",
	bcc="hr-department@eighty-days.com",
	attachment_paths=["C:/Users/me/Docs/hr-guidelines.docx"],
	branding="C:/Users/me/Pics/80d-branding.png",
	branding_tracking_link="https://eighty-days.com/email_landing_page.html"
)
