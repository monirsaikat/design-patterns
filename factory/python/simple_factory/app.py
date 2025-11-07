from .factory import make_notifier, make_notifier_v2


if __name__ == '__main__':
    # emailNotification = make_notifier('email')
    # emailNotification.send('email@gmail.com', 'Welcome :)')

    # smsNotification = make_notifier('sms')
    # smsNotification.send('xxx20933', 'Welcome via SMS')
    
    # n = make_notifier_v2('email')
    # n.send('+xx000000', 'welcome, you are using registry based factory pattern')

    n.send('email@gmail.com', 'this should not be sent!')
    n = make_notifier_v2('push')
    # n.send('username_here', 'message')