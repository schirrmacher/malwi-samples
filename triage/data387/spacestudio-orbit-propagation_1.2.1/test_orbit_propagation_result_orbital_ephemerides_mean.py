# coding: utf-8

"""
    Spacestudio Orbit Propagation API

    <b>CHANGELOG</b> <ul>   <li><b>1.2.0</b> - 2024-06-13 - Add <b>missionDuration</b> field in response payload</li>   <li><b>1.1.5</b> - 2024-06-06 - Improve API documentation</li>   <li><b>1.1.4</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.3</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.2</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.1</b> - 2024-05-28 - Delete <i>NONE</i> solar array type</li>   <li><b>1.1.0</b> - 2024-05-28 - Add perturbations and refactor API</li>   <li><b>1.0.0</b> - 2024-05-27 - Initial version</li> </ul> 

    The version of the OpenAPI document: 1.2.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from spacestudio_orbit_propagation.models.orbit_propagation_result_orbital_ephemerides_mean import OrbitPropagationResultOrbitalEphemeridesMean

class TestOrbitPropagationResultOrbitalEphemeridesMean(unittest.TestCase):
    """OrbitPropagationResultOrbitalEphemeridesMean unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbitPropagationResultOrbitalEphemeridesMean:
        """Test OrbitPropagationResultOrbitalEphemeridesMean
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrbitPropagationResultOrbitalEphemeridesMean`
        """
        model = OrbitPropagationResultOrbitalEphemeridesMean()
        if include_optional:
            return OrbitPropagationResultOrbitalEphemeridesMean(
                keplerian = spacestudio_orbit_propagation.models.keplerian_ephemerides.KeplerianEphemerides(
                    true_anomaly = [
                        1.337
                        ], 
                    mean_anomaly = [
                        1.337
                        ], 
                    inclination = [
                        1.337
                        ], 
                    eccentric_anomaly = [
                        1.337
                        ], 
                    perigee_altitude = [
                        1.337
                        ], 
                    ltan = [
                        1.337
                        ], 
                    altitude = [
                        1.337
                        ], 
                    semi_major_axis = [
                        1.337
                        ], 
                    eccentricity = [
                        1.337
                        ], 
                    raan = [
                        1.337
                        ], ),
                cartesian = spacestudio_orbit_propagation.models.cartesian_ephemerides.CartesianEphemerides(
                    x = [
                        1.337
                        ], 
                    y = [
                        1.337
                        ], 
                    z = [
                        1.337
                        ], 
                    vx = [
                        1.337
                        ], 
                    vy = [
                        1.337
                        ], 
                    vz = [
                        1.337
                        ], )
            )
        else:
            return OrbitPropagationResultOrbitalEphemeridesMean(
        )
        """

    def testOrbitPropagationResultOrbitalEphemeridesMean(self):
        """Test OrbitPropagationResultOrbitalEphemeridesMean"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
