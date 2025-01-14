#
# Test many fickian particles
#

import pybamm
import tests
import unittest


class TestManyParticles(unittest.TestCase):
    def test_public_functions(self):
        param = pybamm.LithiumIonParameters()

        a_n = pybamm.FullBroadcast(
            pybamm.Scalar(1), "negative electrode", {"secondary": "current collector"}
        )
        a_p = pybamm.FullBroadcast(
            pybamm.Scalar(1), "positive electrode", {"secondary": "current collector"}
        )

        variables = {
            "Negative electrode interfacial current density": a_n,
            "Negative electrode temperature": a_n,
            "Negative electrode active material volume fraction": a_n,
            "Negative electrode surface area to volume ratio": a_n,
            "Negative particle radius": a_n,
        }

        submodel = pybamm.particle.no_distribution.FickianDiffusion(param, "Negative")
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()

        variables = {
            "Positive electrode interfacial current density": a_p,
            "Positive electrode temperature": a_p,
            "Positive electrode active material volume fraction": a_p,
            "Positive electrode surface area to volume ratio": a_p,
            "Positive particle radius": a_p,
        }
        submodel = pybamm.particle.no_distribution.FickianDiffusion(param, "Positive")
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
