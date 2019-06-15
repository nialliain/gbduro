from unittest import TestCase
from datetime import datetime
from calculate_results import calculate_results, format_results


class TestCalculateResults(TestCase):

    def test_calculate_results_midStage(self):
        ts = [{
            'displayName': 'Test Rider',
            's1-start': datetime(2019, 1, 1, 8, 0),
            's1-end': '',
            's2-start': '',
            's2-end': '',
            's3-start': '',
            's3-end': '',
            's4-start': '',
            's4-end': '',
        }]
        results = format_results( calculate_results(ts))
        self.assertEqual( 'Test Rider', results[0]['Rider'])
        self.assertEqual( '', results[0]['CP1'])
        self.assertEqual( '', results[0]['CP2'])
        self.assertEqual( '', results[0]['CP3'])
        self.assertEqual( '', results[0]['CP4'])

    def test_calculate_results_afterFirst(self):
        ts = [{
            'displayName': 'Test Rider',
            's1-start': datetime(2019, 1, 1, 8, 0),
            's1-end': datetime(2019, 1, 2, 23, 59),
            's2-start': '',
            's2-end': '',
            's3-start': '',
            's3-end': '',
            's4-start': '',
            's4-end': '',
        }]
        results = format_results( calculate_results(ts))
        self.assertEqual( 'Test Rider', results[0]['Rider'])
        self.assertEqual( '039H 59M', results[0]['CP1'])
        self.assertEqual( '', results[0]['CP2'])
        self.assertEqual( '', results[0]['CP3'])
        self.assertEqual( '', results[0]['CP4'])

    def test_calculate_results_afterSecond(self):
        ts = [{
            'displayName': 'Test Rider',
            's1-start': datetime(2019, 1, 1, 8, 0),
            's1-end': datetime(2019, 1, 2, 23, 59),
            's2-start': datetime(2019, 1, 3, 8, 0),
            's2-end': datetime(2019, 1, 5, 10, 22),
            's3-start': '',
            's3-end': '',
            's4-start': '',
            's4-end': '',
        }]
        results = format_results( calculate_results(ts))
        self.assertEqual( 'Test Rider', results[0]['Rider'])
        self.assertEqual( '039H 59M', results[0]['CP1'])
        self.assertEqual( '090H 21M', results[0]['CP2'])
        self.assertEqual( '', results[0]['CP3'])
        self.assertEqual( '', results[0]['CP4'])

    def test_calculate_results_afterThird(self):
        ts = [{
            'displayName': 'Test Rider',
            's1-start': datetime(2019, 1, 1, 8, 0),
            's1-end': datetime(2019, 1, 2, 23, 59),
            's2-start': datetime(2019, 1, 3, 8, 0),
            's2-end': datetime(2019, 1, 5, 10, 22),
            's3-start': datetime(2019, 1, 6, 8, 0),
            's3-end': datetime(2019, 1, 6, 8, 1),
            's4-start': '',
            's4-end': '',
        }]
        results = format_results( calculate_results(ts))
        self.assertEqual( 'Test Rider', results[0]['Rider'])
        self.assertEqual( '039H 59M', results[0]['CP1'])
        self.assertEqual( '090H 21M', results[0]['CP2'])
        self.assertEqual( '090H 22M', results[0]['CP3'])
        self.assertEqual( '', results[0]['CP4'])

    def test_calculate_results_extraResults(self):
        ts = [{
            'displayName': 'Test Rider',
            's1-start': datetime(2019, 1, 1, 8, 0),
            's1-end': datetime(2019, 1, 2, 23, 59),
            's2-start': datetime(2019, 1, 3, 8, 0),
            's2-end': datetime(2019, 1, 5, 10, 22),
            's3-start': '',
            's3-end': '',
            's4-start': datetime(2019, 1, 6, 8, 0),
            's4-end': datetime(2019, 1, 6, 8, 1),
        }]
        results = format_results( calculate_results(ts))
        self.assertEqual( 'Test Rider', results[0]['Rider'])
        self.assertEqual( '039H 59M', results[0]['CP1'])
        self.assertEqual( '090H 21M', results[0]['CP2'])
        self.assertEqual( '', results[0]['CP3'])
        self.assertEqual( '', results[0]['CP4'])
