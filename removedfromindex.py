import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_email(user_input):
  # print(type(attached))
  email = user_input # st.text_input('Informar o email', 'exemplo@email.com')
  
  file = 'sellout.csv'# pd.read_csv(attached, index_col=[0], header=0, sep=';', dtype='str')
# print(file.head())
  recipients = ['felipe@beanalytic.com.br'] #, 'camila_menezes@steris.com'
  
  message = MIMEMultipart()
  message['Subject'] = f'Arquivo Sellout modificado por {email}'
  message['From'] = 'sistema@beanalytic.com.br'
  message['To'] = ', '.join(recipients)
  message['Bcc'] = 'felipe@beanalytic.com.br'
  message.attach(MIMEText('<h1 style="color: blue">Olá, </a><p>Segue em anexo o Sellout pronto para o Tableau Prep / Dashboard.</p>', 'html'))

  with open(file, 'rb') as attachment:
    payload = MIMEBase('application', 'octat-stream')
    payload.set_payload(attachment.read())
    
  encoders.encode_base64(payload) #encode the attachment
  #add payload header with filename
  payload.add_header('Content-Disposition', f'attachment; filename={file}')
  message.attach(payload)
  # start server
  # context = ssl.create_default_context()
  try:
    with smtplib.SMTP('smtp-legacy.office365.com', 587) as server:
      server.starttls()
      print('server on') 
      server.login(emailConfig.email, emailConfig.password)
      server.sendmail(
        emailConfig.email, 
        recipients, 
        message.as_string())

      attachment.close()
      server.quit()
      st.balloons()
      return True
  except Exception:
    st.warning('Não foi possível enviar o email para Steris, por favor entrar em contato com Steris para informar', icon="⚠️")
    