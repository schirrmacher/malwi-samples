# coding: utf-8

"""
    Spacestudio Orbit Propagation API

    <b>CHANGELOG</b> <ul>   <li><b>1.2.0</b> - 2024-06-13 - Add <b>missionDuration</b> field in response payload</li>   <li><b>1.1.5</b> - 2024-06-06 - Improve API documentation</li>   <li><b>1.1.4</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.3</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.2</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.1</b> - 2024-05-28 - Delete <i>NONE</i> solar array type</li>   <li><b>1.1.0</b> - 2024-05-28 - Add perturbations and refactor API</li>   <li><b>1.0.0</b> - 2024-05-27 - Initial version</li> </ul> 

    The version of the OpenAPI document: 1.2.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from spacestudio_orbit_propagation.models.spacecraft_geometry import SpacecraftGeometry

class TestSpacecraftGeometry(unittest.TestCase):
    """SpacecraftGeometry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpacecraftGeometry:
        """Test SpacecraftGeometry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpacecraftGeometry`
        """
        model = SpacecraftGeometry()
        if include_optional:
            return SpacecraftGeometry(
                type = 'SPHERICAL'
            )
        else:
            return SpacecraftGeometry(
        )
        """

    def testSpacecraftGeometry(self):
        """Test SpacecraftGeometry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
