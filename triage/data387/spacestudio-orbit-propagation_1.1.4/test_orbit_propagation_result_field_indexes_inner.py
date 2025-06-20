# coding: utf-8

"""
    Spacestudio Orbit Propagation API

    <b>CHANGELOG</b> <ul>   <li><b>1.1.4</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.3</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.2</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.1</b> - 2024-05-28 - Delete <i>NONE</i> solar array type</li>   <li><b>1.1.0</b> - 2024-05-28 - Add perturbations and refactor API</li>   <li><b>1.0.0</b> - 2024-05-27 - Initial version</li> </ul> 

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from spacestudio_orbit_propagation.models.orbit_propagation_result_field_indexes_inner import OrbitPropagationResultFieldIndexesInner

class TestOrbitPropagationResultFieldIndexesInner(unittest.TestCase):
    """OrbitPropagationResultFieldIndexesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbitPropagationResultFieldIndexesInner:
        """Test OrbitPropagationResultFieldIndexesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrbitPropagationResultFieldIndexesInner`
        """
        model = OrbitPropagationResultFieldIndexesInner()
        if include_optional:
            return OrbitPropagationResultFieldIndexesInner(
                key = '',
                index = 56
            )
        else:
            return OrbitPropagationResultFieldIndexesInner(
        )
        """

    def testOrbitPropagationResultFieldIndexesInner(self):
        """Test OrbitPropagationResultFieldIndexesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
