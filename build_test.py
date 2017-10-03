import atexit
import unittest
import client

from pact import Consumer, Provider, SomethingLike,Term


pact = Consumer('Consumer').has_pact_with(Provider('Provider'))
pact.start_service()
atexit.register(pact.stop_service)


class GetBuildInfoContract(unittest.TestCase):
 # @unittest.expectedFailure
  def test_get_build(self):
    true = True
    ts = Term('\d+-\d+-\d+T\d+:\d+:\d+.+', u'2017-09-17T19:43:12+03:00')
    expected = {
      u'name':u'#3455',
      u'completed': true, #boolean
    #  u'timestamp': Term('\d+-\d+-\d+T\d+:\d+:\d+.+', u'2017-09-17T19:43:12+03:00'),
      u'info':{
        u'coverage':30,
        u'apiversion':0.1,
        u'swaggerlink':u'http://swagger',
        u'buildtime':230}
    }

    (pact
     .given('build 3455 exists')
     .upon_receiving('a request for build 3455')
     .with_request('get', '/builds/3455')
     .will_respond_with(200, body=expected))


    with pact:
      result = client.build(3455)

    self.assertEqual(result, expected)
