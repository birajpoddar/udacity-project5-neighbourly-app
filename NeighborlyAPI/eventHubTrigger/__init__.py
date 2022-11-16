import json
import logging
import azure.functions as func
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def main(event: func.EventHubEvent):

    # logging.info('Function triggered to process a message: ', event.get_body())
    # logging.info('  EnqueuedTimeUtc =', event.enqueued_time)
    # logging.info('  SequenceNumber =', event.sequence_number)
    # logging.info('  Offset =', event.offset)

    # result = json.dumps({
    #     'id': event.id,
    #     'data': event.get_json(),
    #     'topic': event.topic,
    #     'subject': event.subject,
    #     'event_type': event.event_type,
    # })


    # logging.info('Python EventGrid trigger processed an event: %s', result)

    # logging.critical('Python EventHub trigger processed an event: %s', event.get_body().decode('utf-8'))

    body = event.get_body().decode("UTF-8")
    bodyObj = json.loads(body)

    # Code attributed to SendGrid documentation
    # Sending email
    message = Mail(
        from_email='biraj.poddar@gmail.com',
        to_emails='biraj.poddar@gmail.com',
        subject=f'HTTP Endpoint Triggered - {bodyObj["generator"]}',
        html_content=f'<b>EventGrid Trigger Activated</b><br/> \
            <b>DateTime</b>: {event.enqueued_time} <br/> \
            <b>Message</b> : {bodyObj["message"]} <br/> \
            <b>Generator</b>: {bodyObj["generator"]}')
    try:
        sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        response = sg.send(message)
        logging.info(f'Status code: {response.status_code}')
        logging.info(f'Body: {response.body.decode("UTF-8")}')
        logging.info(f'Headers: {response.headers}')
    except Exception as e:
        logging.error(str(e))



