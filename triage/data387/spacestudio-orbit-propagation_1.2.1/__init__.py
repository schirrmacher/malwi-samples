# coding: utf-8

# flake8: noqa

"""
    Spacestudio Orbit Propagation API

    <b>CHANGELOG</b> <ul>   <li><b>1.2.0</b> - 2024-06-13 - Add <b>missionDuration</b> field in response payload</li>   <li><b>1.1.5</b> - 2024-06-06 - Improve API documentation</li>   <li><b>1.1.4</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.3</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.2</b> - 2024-05-28 - Improve API documentation</li>   <li><b>1.1.1</b> - 2024-05-28 - Delete <i>NONE</i> solar array type</li>   <li><b>1.1.0</b> - 2024-05-28 - Add perturbations and refactor API</li>   <li><b>1.0.0</b> - 2024-05-27 - Initial version</li> </ul> 

    The version of the OpenAPI document: 1.2.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.2.1"

# import apis into sdk package
from spacestudio_orbit_propagation.api.default_api import DefaultApi

# import ApiClient
from spacestudio_orbit_propagation.api_response import ApiResponse
from spacestudio_orbit_propagation.api_client import ApiClient
from spacestudio_orbit_propagation.configuration import Configuration
from spacestudio_orbit_propagation.exceptions import OpenApiException
from spacestudio_orbit_propagation.exceptions import ApiTypeError
from spacestudio_orbit_propagation.exceptions import ApiValueError
from spacestudio_orbit_propagation.exceptions import ApiKeyError
from spacestudio_orbit_propagation.exceptions import ApiAttributeError
from spacestudio_orbit_propagation.exceptions import ApiException

# import models into sdk package
from spacestudio_orbit_propagation.models.advanced_orbit_parameters import AdvancedOrbitParameters
from spacestudio_orbit_propagation.models.axis import Axis
from spacestudio_orbit_propagation.models.body_solar_array import BodySolarArray
from spacestudio_orbit_propagation.models.box_spacecraft_geometry import BoxSpacecraftGeometry
from spacestudio_orbit_propagation.models.cartesian_ephemerides import CartesianEphemerides
from spacestudio_orbit_propagation.models.circular_altitude_orbit_parameters import CircularAltitudeOrbitParameters
from spacestudio_orbit_propagation.models.circular_ground_track_repeated_orbit_parameters import CircularGroundTrackRepeatedOrbitParameters
from spacestudio_orbit_propagation.models.deployable_fixed_solar_array import DeployableFixedSolarArray
from spacestudio_orbit_propagation.models.deployable_rotating_solar_array import DeployableRotatingSolarArray
from spacestudio_orbit_propagation.models.drag_perturbation import DragPerturbation
from spacestudio_orbit_propagation.models.earth_potential_perturbation import EarthPotentialPerturbation
from spacestudio_orbit_propagation.models.elliptical_ground_track_repeated_eccentricity_orbit_parameters import EllipticalGroundTrackRepeatedEccentricityOrbitParameters
from spacestudio_orbit_propagation.models.elliptical_perigee_alt_apogee_alt_orbit_parameters import EllipticalPerigeeAltApogeeAltOrbitParameters
from spacestudio_orbit_propagation.models.elliptical_perigee_alt_eccentricity_orbit_parameters import EllipticalPerigeeAltEccentricityOrbitParameters
from spacestudio_orbit_propagation.models.elliptical_sma_eccentricity_orbit_parameters import EllipticalSmaEccentricityOrbitParameters
from spacestudio_orbit_propagation.models.ephemeris_type import EphemerisType
from spacestudio_orbit_propagation.models.keplerian_ephemerides import KeplerianEphemerides
from spacestudio_orbit_propagation.models.mean_or_osculating_spacecraft_states import MeanOrOsculatingSpacecraftStates
from spacestudio_orbit_propagation.models.mean_or_osculating_spacecraft_states_attitude import MeanOrOsculatingSpacecraftStatesAttitude
from spacestudio_orbit_propagation.models.mean_or_osculating_spacecraft_states_pv_coordinates import MeanOrOsculatingSpacecraftStatesPvCoordinates
from spacestudio_orbit_propagation.models.orbit import Orbit
from spacestudio_orbit_propagation.models.orbit_parameters import OrbitParameters
from spacestudio_orbit_propagation.models.orbit_propagation_request import OrbitPropagationRequest
from spacestudio_orbit_propagation.models.orbit_propagation_request_inputs import OrbitPropagationRequestInputs
from spacestudio_orbit_propagation.models.orbit_propagation_request_outputs import OrbitPropagationRequestOutputs
from spacestudio_orbit_propagation.models.orbit_propagation_request_outputs_orbital_ephemerides import OrbitPropagationRequestOutputsOrbitalEphemerides
from spacestudio_orbit_propagation.models.orbit_propagation_request_outputs_spacecraft_states import OrbitPropagationRequestOutputsSpacecraftStates
from spacestudio_orbit_propagation.models.orbit_propagation_result import OrbitPropagationResult
from spacestudio_orbit_propagation.models.orbit_propagation_result_field_indexes_inner import OrbitPropagationResultFieldIndexesInner
from spacestudio_orbit_propagation.models.orbit_propagation_result_orbital_ephemerides import OrbitPropagationResultOrbitalEphemerides
from spacestudio_orbit_propagation.models.orbit_propagation_result_orbital_ephemerides_mean import OrbitPropagationResultOrbitalEphemeridesMean
from spacestudio_orbit_propagation.models.orbit_propagation_result_orbital_ephemerides_osculating import OrbitPropagationResultOrbitalEphemeridesOsculating
from spacestudio_orbit_propagation.models.orbit_propagation_result_spacecraft_states import OrbitPropagationResultSpacecraftStates
from spacestudio_orbit_propagation.models.perturbation import Perturbation
from spacestudio_orbit_propagation.models.platform import Platform
from spacestudio_orbit_propagation.models.solar_array import SolarArray
from spacestudio_orbit_propagation.models.solar_array_face import SolarArrayFace
from spacestudio_orbit_propagation.models.spacecraft_geometry import SpacecraftGeometry
from spacestudio_orbit_propagation.models.spacecraft_geometry_dimension import SpacecraftGeometryDimension
from spacestudio_orbit_propagation.models.spherical_spacecraft_geometry import SphericalSpacecraftGeometry
from spacestudio_orbit_propagation.models.srp_perturbation import SrpPerturbation
from spacestudio_orbit_propagation.models.third_body_perturbation import ThirdBodyPerturbation
